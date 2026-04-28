[README.md](https://github.com/user-attachments/files/27173340/README.md)

# 👾 CoursePath 🤖

**CoursePath** é uma aplicação de terminal desenvolvida em Python com o objetivo de facilitar o acesso de estudantes da UFRPE a materiais de estudo. A plataforma oferece conteúdos organizados por curso, semestre e disciplina, com suporte integrado à tradução automática de textos e artigos científicos para múltiplos idiomas.

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Fluxo da Aplicação](#-fluxo-da-aplicação)
- [Autenticação e Validações](#-autenticação-e-validações)
- [Banco de Dados](#-banco-de-dados)

---

## ✨ Funcionalidades

### 🔐 Sistema de Autenticação
- **Cadastro** de usuário com validação de nome, e-mail institucional (`NOME.SOBRENOME@UFRPE.BR`) e senha segura
- **Login** com verificação de credenciais no banco de dados
- **Recuperação de senha** diretamente pelo fluxo de login
- **Revisão de dados** pós-cadastro com opção de edição imediata

### ⚙️ Configurações do Usuário
- Alteração de nome, e-mail e senha a qualquer momento
- **Exclusão de conta** com confirmação de segurança

### 📚 Conteúdo por Curso e Disciplina
- Acesso ao curso de **BSI – Bacharelado em Sistemas de Informação**
- Navegação por **semestres** (1º e 2º períodos) e suas respectivas **disciplinas/cadeiras**
- Cada disciplina exibe uma **descrição introdutória** e dá acesso a **2 artigos científicos** relacionados
- Menus com reexibição automática do cabeçalho em caso de opção inválida (via função `imprimir_cabecalho()`)
- Disciplinas disponíveis:
  - **1º Semestre:** Projeto Interdisciplinar, Fundamentos Matemáticos, Princípios de Programação, Sustentabilidade e Sistemas de Informação, Introdução a Sistemas de Administração
  - **2º Semestre:** Projeto Interdisciplinar 02, Fundamentos Matemáticos 02, Fundamentos de Problemas Computacionais, Elementos de Sistemas Computacionais, Fundamentos de Sistemas de Informação

### 🌍 Tradução Integrada
- Tradução automática dos conteúdos e artigos via **Google Translator**
- Suporte a múltiplos idiomas: inglês, português, espanhol, francês, alemão, italiano, russo, japonês, chinês e mais
- Alternância dinâmica entre o idioma traduzido e o **português original** em qualquer tela de conteúdo — inclusive nas telas de cada disciplina individualmente
- **Adição de artigos personalizados:** o usuário pode colar qualquer abstract ou texto, escolher o idioma de destino e receber a tradução instantânea com reexibição do cabeçalho em caso de opção inválida

---

## 📁 Estrutura do Projeto

```
CoursePath/
│
├── main.py                        # Ponto de entrada da aplicação
│
├── menus/                         # Módulos de navegação por menus
│   ├── menuinicial.py             # Tela inicial (cadastro / login / sair)
│   ├── menuprincipal.py           # Menu principal do usuário logado
│   ├── cursos.py                  # Menu de cursos disponíveis (com imprimir_cabecalho)
│   ├── menubsi.py                 # Apresentação do curso de BSI (com imprimir_cabecalho)
│   ├── semestre.py                # Seleção de semestre (com imprimir_cabecalho)
│   ├── menucadeiras.py            # Menus individuais de cada disciplina com textos introdutórios,
│   │                              # artigos e controle de tradução (com imprimir_cabecalho)
│   └── adicionartigos.py          # Fluxo para adicionar e traduzir artigos personalizados
│                                  # (com imprimir_cabecalho)
│
├── cadeiras/                      # Listagem e navegação de cadeiras por período
│   ├── cadeirasperiodo1.py        # Menu de cadeiras do 1º semestre (com imprimir_cabecalho)
│   └── cadeirasperiodo2.py        # Menu de cadeiras do 2º semestre (com imprimir_cabecalho)
│
├── articles/                      # Artigos científicos por disciplina
│   ├── artigos_periodo1.py        # Artigos do 1º período
│   └── artigos_periodo2.py        # Artigos do 2º período
│
├── user/                          # Módulos relacionados ao usuário
│   ├── cadastro.py                # Fluxo de cadastro
│   ├── login.py                   # Fluxo de login e recuperação de senha
│   ├── read.py                    # Leitura e confirmação de dados cadastrados
│   ├── update_fluxo.py            # Atualização de nome e e-mail
│   ├── recoverypassword.py        # Recuperação de senha
│   └── userconfig.py              # Menu de configurações do usuário (CRUD)
│
├── sqlite/                        # Camada de banco de dados
│   └── database.py                # Funções CRUD com SQLite
│
├── others/                        # Utilitários e tradutor
│   ├── utils.py                   # Funções auxiliares e opções de menu variáveis por idioma
│   └── tradutor.py                # Integração com Google Translator
│
└── verifications/                 # Validações de entrada
    └── checagem_email_senha_nome.py  # Regex para e-mail, nome e senha
```

---

## 🛠 Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python 3.x** | Linguagem principal |
| **SQLite3** | Banco de dados local para usuários |
| **deep-translator** | Tradução automática via Google Translator |
| **re (Regex)** | Validação de e-mail, nome e senha |
| **textwrap** | Formatação de texto no terminal |
| **os / time** | Utilitários de sistema e controle de tempo |

---

## 📦 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Biblioteca `deep-translator`:
```bash
pip install deep-translator
```

---

## 🚀 Instalação

**1. Clone o repositório:**
```bash
git clone https://github.com/thuliobandeira402/Coursepath_repository.git
cd Coursepath_repository
```

**2. Instale as dependências:**
```bash
pip install deep-translator
```

**3. Execute a aplicação:**
```bash
python main.py
```

> O banco de dados `banco.db` será criado automaticamente na primeira execução.

---

## 🖥 Como Usar

Ao iniciar o programa, você verá o menu inicial:

```
==================================================
|                👾 COURSEPATH 🤖                |
==================================================
| Escolha:                                       |
|    [1]. Cadastrar-se                           |
|    [2]. Login                                  |
|    [3]. Sair                                   |
==================================================
```

Após o login, o menu principal oferece:

```
[1]. Ver Cursos Disponíveis
[2]. Alterar idioma do menu de cursos
[3]. Alterar dados do usuário
[4]. Adicionar artigo para leitura
[5]. Sair
```

---

## 🔄 Fluxo da Aplicação

```
Menu Inicial
    ├── [1] Cadastro → Validação → Confirmação de dados → (Login)
    ├── [2] Login → Menu Principal
    │       ├── [1] Cursos → BSI → Semestres → Cadeiras → Artigos (+ Tradução)
    │       ├── [2] Alterar idioma global
    │       ├── [3] Configurações do usuário (nome / e-mail / senha / deletar conta)
    │       └── [4] Adicionar artigo → Colar texto → Traduzir
    └── [3] Sair
```

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

### Nome
Deve conter apenas letras (incluindo acentuação) e espaços.

---

## 🗄 Banco de Dados

A aplicação utiliza **SQLite** local com a seguinte estrutura de tabela:

```sql
CREATE TABLE IF NOT EXISTS contas_curso (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
);
```

Operações implementadas (CRUD completo):
- **Create:** cadastro de novo usuário
- **Read:** busca por e-mail, exibição de dados após cadastro
- **Update:** alteração de nome, e-mail e senha
- **Delete:** exclusão de conta com confirmação

---

## 👨‍💻 Autor

Desenvolvido por **Thulio Bandeira**  
Curso: Bacharelado em Sistemas de Informação — UFRPE  
Repositório: [github.com/thuliobandeira402/Coursepath_repository](https://github.com/thuliobandeira402/Coursepath_repository)
