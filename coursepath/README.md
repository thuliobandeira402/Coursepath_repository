# CoursePath 📚

Sistema de gerenciamento de artigos acadêmicos para estudantes de SI/UFRPE.
Backend Flask (POO) + Frontend HTML/CSS/JS puro, integração com Claude API.

---

## Estrutura

```
coursepath/
├── backend/
│   ├── app.py              ← servidor Flask (API REST)
│   ├── database.py         ← classes Database, UserRepository, ArticleRepository
│   └── seed_articles.py    ← artigos dos 2 semestres
└── frontend/
    ├── index.html          ← tela de login/cadastro
    ├── pages/
    │   └── dashboard.html  ← app principal
    ├── css/
    │   ├── style.css       ← globals + auth
    │   └── dashboard.css   ← layout do app
    └── js/
        ├── api.js          ← comunicação com backend
        ├── auth.js         ← login e cadastro
        └── dashboard.js    ← artigos, modal, resumo, quiz
```

---

## Como rodar

### 1. Instale as dependências

```bash
pip install flask
```

### 2. Inicie o servidor backend

```bash
cd backend
python app.py
```

O servidor sobe em **http://localhost:5000**

### 3. Abra o frontend

Você tem 2 opções:

**Opção A — extensão Live Server (VS Code)**  
Clique com botão direito em `frontend/index.html` → "Open with Live Server"

**Opção B — servidor HTTP simples do Python**
```bash
cd frontend
python -m http.server 8080
```
Acesse: http://localhost:8080

---

## Funcionalidades implementadas

| Funcionalidade | Detalhe |
|---|---|
| ✅ Login / Cadastro | Validação com regex (email @ufrpe.br, senha forte) |
| ✅ POO no backend | Classes `Database`, `UserRepository`, `ArticleRepository` |
| ✅ Banco melhorado | 4 tabelas: `users`, `articles`, `read_articles`, `favorite_articles` |
| ✅ Artigos por semestre | Filtro por 1º e 2º semestre na sidebar |
| ✅ Artigos lidos | Tabela separada, listagem dedicada no menu |
| ✅ Favoritos | Toggle, listagem separada, ícone no card |
| ✅ Resumo com IA | Chama Claude API, exibe com markdown renderizado |
| ✅ Quiz | Gerado por IA, só disponível após marcar como lido |
| ✅ Filtro por disciplina | Tags clicáveis por cadeira |
| ✅ Busca em tempo real | Filtra por título, autor, disciplina, conteúdo |
| ✅ Frontend integrado | Fetch API, sessão via cookie Flask |

---

## Regras de negócio

- **Resumo**: disponível a qualquer momento ao abrir um artigo
- **Quiz**: só aparece após marcar o artigo como lido
- **Email**: obrigatoriamente no formato `nome.sobrenome@ufrpe.br`
- **Senha**: mínimo 8 chars, 1 maiúscula, 1 minúscula, 1 número, 1 símbolo
