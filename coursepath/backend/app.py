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

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False

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

# ── Gemini API config ──────────────────────────────────────────────────────────
GEMINI_API_KEY = "AQ.Ab8RN6JVs723lLHO3mg1X-D-wIbZ_RtlBB9UcR-GHqwGSGIWSQ"

GEMINI_MODEL   = "gemini-2.5-flash"
GEMINI_API_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
)
GEMINI_HEADERS = {"Content-Type": "application/json"}
# ──────────────────────────────────────────────────────────────────────────────


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

def _call_gemini(prompt, max_tokens=1000):
    """Chama a API do Gemini e retorna o texto gerado."""
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens}
    }).encode("utf-8")
    req = urllib.request.Request(
        GEMINI_API_URL,
        data=payload,
        method="POST",
        headers=GEMINI_HEADERS
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
    return result["candidates"][0]["content"]["parts"][0]["text"]


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


# USERS (CRUD)

@app.route("/api/user", methods=["GET"])
def get_user():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)
    user = user_repo.get_by_id(user_id)
    if not user:
        return _json({"error": "Usuário não encontrado."}, 404)
    return _json({"user": user})


@app.route("/api/user", methods=["PUT"])
def update_user():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    data = request.get_json() or {}
    name     = (data.get("name") or "").strip() or None
    email    = (data.get("email") or "").strip().lower() or None
    password = (data.get("password") or "").strip() or None

    if name is not None and not re.match(r"^[A-Za-zÀ-ÿ ]+$", name):
        return _json({"error": "Nome inválido. Use apenas letras e espaços."}, 400)
    if email is not None and not _validate_email(email):
        return _json({"error": "Email deve seguir o formato NOME.SOBRENOME@UFRPE.BR"}, 400)
    if password is not None and not _validate_password(password):
        return _json({"error": "Senha deve ter 8+ caracteres, maiúscula, minúscula, número e símbolo."}, 400)

    # Verifica se email já existe (por outro usuário)
    if email is not None:
        existing = user_repo.get_by_email(email)
        if existing and existing["id"] != user_id:
            return _json({"error": "Email já cadastrado por outro usuário."}, 409)

    user_repo.update(user_id, name=name, email=email, password=password)

    # Atualiza sessão se nome mudou
    if name is not None:
        session["user_name"] = name

    user = user_repo.get_by_id(user_id)
    return _json({"message": "Perfil atualizado com sucesso.", "user": user})


@app.route("/api/user", methods=["DELETE"])
def delete_user():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    data = request.get_json() or {}
    password = (data.get("password") or "").strip()

    if not user_repo.verify_password(user_id, password):
        return _json({"error": "Senha incorreta. Confirme sua senha para excluir a conta."}, 403)

    user_repo.delete(user_id)
    session.clear()
    return _json({"message": "Conta excluída com sucesso."})


# TRANSLATION

@app.route("/api/articles/<int:article_id>/translate", methods=["GET"])
def translate_introduction(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    if not TRANSLATOR_AVAILABLE:
        return _json({"error": "Biblioteca de tradução não instalada. Execute: pip install deep-translator"}, 503)

    article = article_repo.get_by_id(article_id)
    if not article:
        return _json({"error": "Artigo não encontrado."}, 404)

    target_lang = request.args.get("lang", "pt")

    try:
        translator = GoogleTranslator(source="auto", target=target_lang)
        translated = translator.translate(article["introduction"])
        return _json({
            "article_id": article_id,
            "original": article["introduction"],
            "translated": translated,
            "target_lang": target_lang
        })
    except Exception as e:
        return _json({"error": f"Erro na tradução: {str(e)}"}, 500)


# SUMMARY

@app.route("/api/articles/<int:article_id>/summary", methods=["GET"])
def get_summary(article_id):
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    article = article_repo.get_by_id(article_id)
    if not article:
        return _json({"error": "Artigo não encontrado."}, 404)

    prompt = f"""Você é um assistente acadêmico de Sistemas de Informação.
Gere um resumo didático e estruturado em português do artigo abaixo.

IMPORTANTE: Comece DIRETAMENTE com o resumo. Não escreva frases introdutórias como "Como assistente..." ou "Apresento o resumo...". Vá direto ao conteúdo.

Artigo:
Título: {article['title']}
Autores: {article['authors']}
Disciplina: {article['subject']} — {article['semester']}º Semestre

Introdução:
{article['introduction']}

Estruture o resumo com estas 3 seções (use os títulos exatos):

## Visão Geral
[Explique o que o artigo aborda em 2-3 parágrafos]

## Principais Conceitos
[Liste os conceitos mais importantes com breve explicação de cada um]

## Relevância Acadêmica
[Explique por que este artigo é importante para estudantes de Sistemas de Informação]"""

    try:
        summary = _call_gemini(prompt, max_tokens=3000)
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
        text = _call_gemini(prompt, max_tokens=2000)
        text = re.sub(r"```json|```", "", text).strip()
        quiz = json.loads(text)
        return _json(quiz)
    except json.JSONDecodeError as e:
        return _json({"error": f"Erro ao parsear quiz: {str(e)}"}, 500)
    except Exception as e:
        return _json({"error": f"Erro ao gerar quiz: {str(e)}"}, 500)


@app.route("/api/articles", methods=["POST"])
def create_article():
    user_id = _require_auth()
    if not user_id:
        return _json({"error": "Não autenticado."}, 401)

    data = request.get_json()
    title        = (data.get("title") or "").strip()
    authors      = (data.get("authors") or "").strip()
    introduction = (data.get("introduction") or "").strip()
    link         = (data.get("link") or "").strip()
    subject      = (data.get("subject") or "").strip()
    semester     = data.get("semester")

    if not title:
        return _json({"error": "Título é obrigatório."}, 400)
    if not authors:
        return _json({"error": "Autores são obrigatórios."}, 400)
    if not introduction:
        return _json({"error": "Introdução é obrigatória."}, 400)
    if not link:
        return _json({"error": "Link é obrigatório."}, 400)
    if not subject:
        return _json({"error": "Disciplina é obrigatória."}, 400)
    if semester not in (1, 2):
        return _json({"error": "Semestre deve ser 1 ou 2."}, 400)

    article_repo.db.execute(
        "INSERT INTO articles (title, authors, introduction, link, subject, semester) VALUES (?, ?, ?, ?, ?, ?)",
        (title, authors, introduction, link, subject, semester)
    )
    return _json({"message": "Artigo criado com sucesso."}, 201)


if __name__ == "__main__":
    print("CoursePath API rodando em http://localhost:5000")
    app.run(debug=True, port=5000)
