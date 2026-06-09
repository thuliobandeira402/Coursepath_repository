# 👾 CoursePath 🤖

**CoursePath** é uma plataforma web voltada à agregação de conteúdos educacionais e à redução de barreiras linguísticas por meio de tradução dinâmica. A plataforma centraliza materiais acadêmicos organizados por semestre e disciplina para estudantes da UFRPE, integrando funcionalidades de inteligência artificial para geração de resumos e quizzes automáticos via API do Gemini.

> **Release 2** — versão web completa, evoluída a partir da aplicação de terminal da Release 1.

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Fluxo da Aplicação](#-fluxo-da-aplicação)
- [API REST](#-api-rest)
- [Autenticação e Validações](#-autenticação-e-validações)
- [Banco de Dados](#-banco-de-dados)

---

## ✨ Funcionalidades

### 🔐 Sistema de Autenticação
- **Cadastro** de usuário com validação de nome, e-mail institucional (`NOME.SOBRENOME@UFRPE.BR`) e senha segura
- **Login** com verificação de credenciais e **CAPTCHA matemático** de segurança
- **Recuperação de senha** diretamente pelo fluxo de login
- **Gerenciamento de perfil** pelo dashboard: alteração de nome, e-mail e senha; exclusão de conta com confirmação

### 📚 Conteúdo por Semestre e Disciplina
- Navegação por **1º e 2º semestres** com artigos organizados por disciplina
- **Filtragem** de artigos por semestre, disciplina ou nome via campo de busca
- **Marcação de artigos como lidos** com listagem separada de artigos já lidos
- **Sistema de favoritos**: adicionar/remover artigos favoritos e acessá-los em aba dedicada
- **Adição de artigos externos** pelo próprio usuário, com campos de título, autores, disciplina, semestre, introdução e URL

### 🌍 Tradução Dinâmica
- Tradução automática da introdução dos artigos via **Google Translator** (`deep-translator`)
- Suporte a múltiplos idiomas: inglês, espanhol, francês, alemão, italiano, russo, japonês, chinês, entre outros
- Alternância dinâmica entre o idioma traduzido e o **português original** sem sair da tela

### 🤖 Inteligência Artificial (API Gemini)
- **Geração de resumo acadêmico** contextualizado à disciplina e ao semestre, estruturado em três seções: Visão Geral, Principais Conceitos e Relevância Acadêmica
- **Geração automática de quiz** de múltipla escolha com 5 questões — disponível apenas após o artigo ser marcado como lido — com alternativas, resposta correta e explicação

---

## 📁 Estrutura do Projeto

```
coursepath/
│
├── backend/
│   ├── app.py               # API REST Flask — todas as rotas da aplicação
│   ├── database.py          # Gerenciamento do banco SQLite3 (UserRepository, ArticleRepository)
│   ├── seed_articles.py     # Artigos iniciais pré-carregados no banco
│   └── requirements.txt     # Dependências Python do backend
│
├── frontend/
│   ├── index.html           # Tela de login e cadastro
│   └── pages/
│       └── dashboard.html   # Dashboard principal (artigos, perfil, quiz, tradução)
│
├── css/
│   ├── style.css            # Estilos globais e tela de autenticação
│   └── dashboard.css        # Estilos do dashboard
│
├── js/
│   ├── api.js               # Funções de consumo da API REST
│   ├── auth.js              # Lógica de autenticação (login, cadastro, CAPTCHA)
│   ├── dashboard.js         # Interface do dashboard (artigos, quiz, tradução, favoritos)
│   └── profile.js           # Gerenciamento de perfil do usuário
│
└── coursepath.db            # Banco de dados SQLite3 (gerado automaticamente)
```

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3.x** | Linguagem principal do backend |
| **Flask** | Framework web para a API REST |
| **Flask-CORS** | Compartilhamento de recursos entre origens (frontend ↔ backend) |
| **SQLite3** | Banco de dados local para usuários e artigos |
| **deep-translator** | Tradução automática via Google Translator |
| **Gemini API** | Geração de resumos e quizzes com IA (modelo `gemini-2.5-flash`) |
| **urllib.request** | Requisições HTTP à API do Gemini (sem dependência extra) |
| **re (Regex)** | Validação de e-mail e senha; limpeza de resposta JSON do Gemini |
| **hashlib** | Criptografia de senhas |
| **HTML5 / CSS3 / JavaScript** | Frontend completo da aplicação |

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Um servidor local para o frontend (ex: extensão **Live Server** do VS Code)

---

## 🚀 Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/thuliobandeira402/Coursepath_repository.git
cd Coursepath_repository
```

**2. Instale as dependências do backend:**
```bash
pip install flask flask-cors deep-translator
```

Ou via arquivo de requirements:
```bash
pip install -r backend/requirements.txt
```

**3. Inicie o backend:**
```bash
cd backend
python app.py
```

> O banco de dados `coursepath.db` será criado e populado automaticamente na primeira execução.

**4. Abra o frontend:**

Abra `frontend/index.html` com o Live Server (VS Code) ou qualquer servidor HTTP local. O backend deve estar rodando em `http://localhost:5000`.

---

## 🖥 Como Usar

Ao acessar a aplicação, você verá a tela de autenticação:

- **Cadastro:** preencha nome, e-mail institucional (`nome.sobrenome@ufrpe.br`) e senha
- **Login:** informe e-mail, senha e resolva o CAPTCHA matemático exibido

Após autenticado, o dashboard oferece:

- **Sidebar** com navegação entre: Todos os Artigos, 1º Semestre, 2º Semestre, Artigos Lidos e Favoritos
- **Campo de busca** para filtrar por título, disciplina ou autor
- **Cards de artigo** com opções de: abrir PDF, marcar como lido, favoritar e traduzir introdução
- **Modal do artigo** com tradução dinâmica, geração de resumo via IA e quiz automático (após leitura)
- **Perfil do usuário** acessível pelo chip no topo da sidebar (editar dados ou excluir conta)
- **Adicionar artigo externo** pelo botão dedicado no dashboard

---

## 🔄 Fluxo da Aplicação

```
Tela de Login / Cadastro
    ├── Cadastro → Validação (e-mail, senha, nome) → Redirecionamento ao Login
    └── Login (+ CAPTCHA) → Dashboard
            ├── Todos os Artigos / 1º Semestre / 2º Semestre
            │       └── Card do Artigo
            │               ├── Traduzir Introdução (idioma selecionável)
            │               ├── Marcar como Lido
            │               ├── Favoritar
            │               ├── Gerar Resumo com IA
            │               └── Gerar Quiz com IA (requer artigo lido)
            ├── Artigos Lidos
            ├── Favoritos
            ├── Adicionar Artigo Externo
            └── Perfil → Editar nome / e-mail / senha / Excluir conta
```

---

## 🔌 API REST

O backend expõe uma API REST em `http://localhost:5000`. Principais endpoints:

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/api/register` | Cadastro de usuário |
| `POST` | `/api/login` | Login com sessão |
| `POST` | `/api/logout` | Logout |
| `GET` | `/api/me` | Dados do usuário autenticado |
| `GET` | `/api/articles` | Listar artigos (parâmetro `?semester=1` ou `2`) |
| `GET` | `/api/articles/<id>` | Detalhe de um artigo |
| `POST` | `/api/articles` | Adicionar artigo externo |
| `POST` | `/api/articles/<id>/read` | Marcar artigo como lido |
| `GET` | `/api/articles/read` | Listar artigos lidos |
| `POST` | `/api/articles/<id>/favorite` | Alternar favorito |
| `GET` | `/api/articles/favorites` | Listar favoritos |
| `GET` | `/api/articles/<id>/translate` | Traduzir introdução (parâmetro `?lang=en`) |
| `GET` | `/api/articles/<id>/summary` | Gerar resumo com IA |
| `POST` | `/api/articles/<id>/quiz` | Gerar quiz com IA (requer artigo lido) |
| `GET` | `/api/user` | Dados do perfil |
| `PUT` | `/api/user` | Atualizar nome, e-mail ou senha |
| `DELETE` | `/api/user` | Excluir conta |

---

## 🔒 Autenticação e Validações

### E-mail
Deve seguir o formato institucional da UFRPE:
```
NOME.SOBRENOME@UFRPE.BR
```

### Senha
Deve conter no mínimo:
- 8 caracteres
- 1 letra maiúscula
- 1 letra minúscula
- 1 número
- 1 caractere especial (`!@#$%^&*` etc.)

### CAPTCHA
Operação matemática simples gerada dinamicamente no login para impedir automações.

### Senhas no banco
Armazenadas com hash via **hashlib** — nunca em texto puro.

---

## 🗄 Banco de Dados

A aplicação utiliza **SQLite3** local. As principais tabelas são:

```sql
-- Usuários
CREATE TABLE IF NOT EXISTS users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    nome     TEXT NOT NULL,
    email    TEXT UNIQUE NOT NULL,
    senha    TEXT NOT NULL
);

-- Artigos
CREATE TABLE IF NOT EXISTS articles (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT NOT NULL,
    authors      TEXT,
    subject      TEXT,
    semester     INTEGER,
    introduction TEXT,
    url          TEXT
);

-- Status por usuário (lido / favorito)
CREATE TABLE IF NOT EXISTS article_status (
    user_id    INTEGER,
    article_id INTEGER,
    is_read    BOOLEAN DEFAULT 0,
    is_favorite BOOLEAN DEFAULT 0,
    PRIMARY KEY (user_id, article_id)
);
```

---

## 👨‍💻 Autores

Desenvolvido por **Thulio Bandeira e Rivan Barroso**
Curso: Bacharelado em Sistemas de Informação — UFRPE
Repositório: [github.com/thuliobandeira402/Coursepath_repository](https://github.com/thuliobandeira402/Coursepath_repository)
Acesse o Drive: [https://drive.google.com/drive/u/1/folders/17BP3I00TOmk3vYRExs75DUxPmVBqaOv5](https://drive.google.com/drive/u/1/folders/17BP3I00TOmk3vYRExs75DUxPmVBqaOv5)
