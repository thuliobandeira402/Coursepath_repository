"""
CoursePath - Backend Flask (API REST)
"""
import re
import json
import urllib.request
from flask import Flask, request, jsonify, session
from flask_cors import CORS

from database import get_db, UserRepository, ArticleRepository
from seed_articles import ARTICLES

app = Flask(__name__)
app.secret_key = "coursepath-secret-2025"
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = False

CORS(app,
     supports_credentials=True,
     origins=["http://127.0.0.1:5500", "http://localhost:5500",
               "http://127.0.0.1:5000", "http://localhost:5000",
               "null"])

db = get_db()
user_repo = UserRepository(db)
article_repo = ArticleRepository(db)
article_repo.seed(ARTICLES)

API_KEY = "gemini-3-flash-preview"
API_HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01"
}


def _json(data, status=200):
    return jsonify(data), status

def _validate_email(email):
    return bool(re.match(r"^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$", email, re.IGNORECASE))

def _validate_password(pwd):
    return (len(pwd) >= 8
            and any(c.isupper() for c in pwd)
            and any(c.islower() for c in pwd)
            and any(c.isdigit() for c in pwd)
            and any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in pwd))

def _require_auth():
    user_id = session.get("user_id")
    if user_id:
        return user_id
    header_id = request.headers.get("X-User-Id")
    if header_id and header_id.isdigit():
        return int(header_id)
    return None

def _call_claude(prompt, max_tokens=1000):
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        method="POST",
        headers=API_HEADERS
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    return result["content"][0]["text"]


# AUTH

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()

    if not name or not re.match(r"^[A-Za-zÀ-ÿ ]+$", name):
        return _json({"error": "Nome inválido. Use apenas letras e espaços."}, 400)
    if not _validate_email(email):
        return _json({"error": "Email deve seguir o formato NOME.SOBRENOME@UFRPE.BR"}, 400)
    if not _validate_password(password):
        return _json({"error": "Senha deve ter 8+ caracteres, maiúscula, minúscula, número e símbolo."}, 400)

    ok, msg = user_repo.create(name, email, password)
    if not ok:
        return _json({"error": msg}, 409)
    return _json({"message": msg})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = (data.get("email") or "").strip().lower()
    password = (data.get("password") or "").strip()

    user = user_repo.authenticate(email, password)
    if not user:
        return _json({"error": "Email ou senha incorretos."}, 401)

    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    return _json({"user": {"id": user["id"], "name": user["name"], "email": user["email"]}})


@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return _json({"message": "Logout realizado."})


@app.route("/api/me", methods=["GET"])
def me():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    return _json({"user_id": user_id, "name": session.get("user_name")})


# ARTICLES

@app.route("/api/articles", methods=["GET"])
def list_articles():
    user_id = _require_auth()
    semester = request.args.get("semester", type=int)
    articles = article_repo.get_by_semester(semester) if semester else article_repo.get_all()

    for a in articles:
        if user_id:
            status = article_repo.get_article_status(user_id, a["id"])
            a["is_read"] = status["is_read"]
            a["is_favorite"] = status["is_favorite"]
        else:
            a["is_read"] = False
            a["is_favorite"] = False

    return _json(articles)


@app.route("/api/articles/<int:article_id>", methods=["GET"])
def get_article(article_id):
    user_id = _require_auth()
    article = article_repo.get_by_id(article_id)
    if not article:
        return _json({"error": "Artigo não encontrado."}, 404)
    if user_id:
        status = article_repo.get_article_status(user_id, article_id)
        article["is_read"] = status["is_read"]
        article["is_favorite"] = status["is_favorite"]
    return _json(article)


# READ / FAVORITES

@app.route("/api/articles/<int:article_id>/read", methods=["POST"])
def mark_read(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    article_repo.mark_as_read(user_id, article_id)
    return _json({"message": "Marcado como lido."})


@app.route("/api/articles/read", methods=["GET"])
def list_read():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    return _json(article_repo.get_read_articles(user_id))


@app.route("/api/articles/<int:article_id>/favorite", methods=["POST"])
def toggle_favorite(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    is_fav = article_repo.toggle_favorite(user_id, article_id)
    return _json({"favorited": is_fav})


@app.route("/api/articles/favorites", methods=["GET"])
def list_favorites():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    articles = article_repo.get_favorites(user_id)
    for a in articles:
        a["is_favorite"] = True
        a["is_read"] = article_repo.is_read(user_id, a["id"])
    return _json(articles)


# SUMMARY

@app.route("/api/articles/<int:article_id>/summary", methods=["GET"])
def get_summary(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    article = article_repo.get_by_id(article_id)
    if not article:
        return _json({"error": "Artigo não encontrado."}, 404)

    prompt = f"""Você é um assistente acadêmico especializado em Sistemas de Informação.
Gere um resumo didático e estruturado do seguinte artigo acadêmico em português:

Título: {article['title']}
Autores: {article['authors']}
Disciplina: {article['subject']} (Semestre {article['semester']})

Introdução/Contexto:
{article['introduction']}

Forneça um resumo em 3 seções:
1. **Visão Geral**: O que o artigo aborda
2. **Principais Conceitos**: Lista dos conceitos importantes
3. **Relevância Acadêmica**: Por que é importante para estudantes de SI"""

    try:
        summary = _call_claude(prompt, max_tokens=1000)
        return _json({"summary": summary, "article_id": article_id})
    except Exception as e:
        return _json({"error": f"Erro ao gerar resumo: {str(e)}"}, 500)


# QUIZ

@app.route("/api/articles/<int:article_id>/quiz", methods=["POST"])
def generate_quiz(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    if not article_repo.is_read(user_id, article_id):
        return _json({"error": "Marque o artigo como lido antes de fazer o quiz."}, 403)

    article = article_repo.get_by_id(article_id)
    if not article:
        return _json({"error": "Artigo não encontrado."}, 404)

    data = request.get_json() or {}
    summary = data.get("summary", "")

    prompt = f"""Você é um professor universitário de Sistemas de Informação.
Crie um quiz de 5 questões de múltipla escolha sobre o artigo:

Título: {article['title']}
Disciplina: {article['subject']}
Conteúdo: {article['introduction']}
{f"Resumo: {summary}" if summary else ""}

Retorne APENAS um JSON válido neste formato exato:
{{
  "questions": [
    {{
      "question": "Texto da pergunta",
      "options": ["A) opção", "B) opção", "C) opção", "D) opção"],
      "correct": 0,
      "explanation": "Explicação"
    }}
  ]
}}"""

    try:
        text = _call_claude(prompt, max_tokens=2000)
        text = re.sub(r"```json|```", "", text).strip()
        quiz = json.loads(text)
        return _json(quiz)
    except json.JSONDecodeError as e:
        return _json({"error": f"Erro ao parsear quiz: {str(e)}"}, 500)
    except Exception as e:
        return _json({"error": f"Erro ao gerar quiz: {str(e)}"}, 500)


if __name__ == "__main__":
    print("CoursePath API rodando em http://localhost:5000")
    app.run(debug=True, port=5000)
