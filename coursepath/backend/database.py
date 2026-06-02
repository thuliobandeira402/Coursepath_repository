"""
CoursePath - Camada de banco de dados (POO)
Tabelas: users, articles, read_articles, favorite_articles
"""
import sqlite3
import hashlib
import os
from datetime import datetime


class Database:
    """Gerencia a conexão e criação das tabelas."""

    DB_PATH = "coursepath.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT NOT NULL,
                email   TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS articles (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       TEXT NOT NULL,
                authors     TEXT NOT NULL,
                introduction TEXT NOT NULL,
                link        TEXT NOT NULL,
                subject     TEXT NOT NULL,
                semester    INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS read_articles (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                article_id  INTEGER NOT NULL,
                read_at     TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (article_id) REFERENCES articles(id),
                UNIQUE (user_id, article_id)
            );

            CREATE TABLE IF NOT EXISTS favorite_articles (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL,
                article_id  INTEGER NOT NULL,
                favorited_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (article_id) REFERENCES articles(id),
                UNIQUE (user_id, article_id)
            );
        """)
        self.conn.commit()

    def execute(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return cur

    def fetchone(self, sql, params=()):
        return self.execute(sql, params).fetchone()

    def fetchall(self, sql, params=()):
        return self.execute(sql, params).fetchall()

    def close(self):
        self.conn.close()


# Singleton global
_db_instance = None

def get_db() -> Database:
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance


class UserRepository:
    """CRUD de usuários."""

    def __init__(self, db: Database):
        self.db = db

    def _hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def create(self, name: str, email: str, password: str):
        try:
            self.db.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, self._hash(password))
            )
            return True, "Usuário criado com sucesso."
        except sqlite3.IntegrityError:
            return False, "Email já cadastrado."

    def authenticate(self, email: str, password: str):
        row = self.db.fetchone(
            "SELECT * FROM users WHERE email = ? AND password = ?",
            (email, self._hash(password))
        )
        return dict(row) if row else None

    def get_by_email(self, email: str):
        row = self.db.fetchone("SELECT id, name, email FROM users WHERE email = ?", (email,))
        return dict(row) if row else None

    def email_exists(self, email: str) -> bool:
        return self.db.fetchone("SELECT id FROM users WHERE email = ?", (email,)) is not None


class ArticleRepository:
    """CRUD de artigos + artigos lidos + favoritos."""

    def __init__(self, db: Database):
        self.db = db

    def seed(self, articles: list):
        """Popula artigos se a tabela estiver vazia."""
        count = self.db.fetchone("SELECT COUNT(*) as c FROM articles")["c"]
        if count == 0:
            for a in articles:
                self.db.execute(
                    "INSERT INTO articles (title, authors, introduction, link, subject, semester) VALUES (?, ?, ?, ?, ?, ?)",
                    (a["title"], a["authors"], a["introduction"], a["link"], a["subject"], a["semester"])
                )

    def get_all(self):
        rows = self.db.fetchall("SELECT * FROM articles ORDER BY semester, subject, id")
        return [dict(r) for r in rows]

    def get_by_id(self, article_id: int):
        row = self.db.fetchone("SELECT * FROM articles WHERE id = ?", (article_id,))
        return dict(row) if row else None

    def get_by_semester(self, semester: int):
        rows = self.db.fetchall("SELECT * FROM articles WHERE semester = ? ORDER BY subject, id", (semester,))
        return [dict(r) for r in rows]

    # ---------- lidos ----------
    def mark_as_read(self, user_id: int, article_id: int):
        try:
            self.db.execute(
                "INSERT OR IGNORE INTO read_articles (user_id, article_id) VALUES (?, ?)",
                (user_id, article_id)
            )
            return True
        except Exception:
            return False

    def get_read_articles(self, user_id: int):
        rows = self.db.fetchall(
            """SELECT a.*, ra.read_at FROM articles a
               JOIN read_articles ra ON a.id = ra.article_id
               WHERE ra.user_id = ? ORDER BY ra.read_at DESC""",
            (user_id,)
        )
        return [dict(r) for r in rows]

    def is_read(self, user_id: int, article_id: int) -> bool:
        return self.db.fetchone(
            "SELECT id FROM read_articles WHERE user_id = ? AND article_id = ?",
            (user_id, article_id)
        ) is not None

    # ---------- favoritos ----------
    def toggle_favorite(self, user_id: int, article_id: int):
        exists = self.db.fetchone(
            "SELECT id FROM favorite_articles WHERE user_id = ? AND article_id = ?",
            (user_id, article_id)
        )
        if exists:
            self.db.execute(
                "DELETE FROM favorite_articles WHERE user_id = ? AND article_id = ?",
                (user_id, article_id)
            )
            return False  # removido
        else:
            self.db.execute(
                "INSERT INTO favorite_articles (user_id, article_id) VALUES (?, ?)",
                (user_id, article_id)
            )
            return True  # adicionado

    def get_favorites(self, user_id: int):
        rows = self.db.fetchall(
            """SELECT a.*, fa.favorited_at FROM articles a
               JOIN favorite_articles fa ON a.id = fa.article_id
               WHERE fa.user_id = ? ORDER BY fa.favorited_at DESC""",
            (user_id,)
        )
        return [dict(r) for r in rows]

    def is_favorite(self, user_id: int, article_id: int) -> bool:
        return self.db.fetchone(
            "SELECT id FROM favorite_articles WHERE user_id = ? AND article_id = ?",
            (user_id, article_id)
        ) is not None

    def get_article_status(self, user_id: int, article_id: int) -> dict:
        return {
            "is_read": self.is_read(user_id, article_id),
            "is_favorite": self.is_favorite(user_id, article_id)
        }
