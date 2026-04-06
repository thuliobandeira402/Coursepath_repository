import re
import sqlite3

def menu_inicial():
    print("="*50)
    print("            COURSEPATH")
    print("="*50)
    print("""Escolha:  
    1. Cadastrar-se
    2. Login
    3. Sair""")
    escolha = input("Opção: ").strip()
    while escolha not in ["1", "2", "3"]:
        print("Opção inválida. Tente novamente.")
        escolha = input("Opção: ").strip()
    return escolha

def criar_tabela(): #Criar tabela de usuários para cadastro no banco de dados
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS contas_curso (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            senha TEXT NOT NULL
                        )""")
    connection.commit()
    connection.close()

def fazer_cadastro(): #Todo o fluxo do cadastro(diminuir linhas da main)
    #fiz primeiramente o código utilizando ifs aninhados, porém após revisar o código com a claude resolvi mudar para a metodologia early return
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return

    email = input("Email: ").strip()
    if not check_email(email):
        print("Email inválido! O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR")
        return

    senha = input("Senha: ").strip()
    if not check_senha(senha):
        print("""Senha inválida! A senha deve conter pelo menos 8 caracteres,
uma letra maiúscula, uma letra minúscula, um número e um caractere especial.""")
        return

    repetir_senha = input("Repita a senha: ").strip()
    if senha != repetir_senha:
        print("As senhas não coincidem.")
        return

    if not cadastrar_usuario(nome, email, senha):
        print("Erro ao cadastrar usuário.")
        return
# Aqui termina o cadastro e inicia o U do CRUD, onde o usuário pode atualizar seus dados cadastrados
    print("Cadastro realizado com sucesso!")
    usuario = buscar_usuario_por_email(email)
    print("\n CONFIRA SEUS DADOS CADASTRADOS:")
    print(f"  Nome:  {usuario[0]}")
    print(f"  Email: {usuario[1]}")
    print("="*50)
    print("""Deseja alterar algum dado cadastrado?
    1. Sim
    2. Não (Sair e fazer login)""")
    if input("Opção: ").strip() == "2":
        print("Faça login para acessar sua conta.")
        return
    atualizar_dados(email)

def check_email(email):
    # email precisa seguir a formatação NOME.SOBRENOME@UFRPE.BR
    regra_email = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@[uU][fF][rR][pP][eE]\.[bB][rR]$')
    ve = re.fullmatch(regra_email, email)
    if ve:
        return True
    else:
        return False

def check_senha(senha):
    # Senha precisa ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere 
    # especial
    if len(senha) < 8:
        return False
    elif not re.search(r'[A-Z]', senha):
        return False
    elif not re.search(r'[a-z]', senha):    
        return False
    elif not re.search(r'[0-9]', senha):
        return False
    elif not re.search(r'[!@#$%^&*(),.?"{}|<>]', senha):
        return False
    else:
        return True

def cadastrar_usuario(nome, email, senha):
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    # Tentar cadastrar o usuário, mas se o email já existir, mostrar essa mensagem de erro
    try:
        cursor.execute("INSERT INTO contas_curso (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        connection.close()
        print("Erro: Email já cadastrado.")
        return False
    
def buscar_usuario_por_email(email): # Buscar por algum usuario no banco de dados(a ideia é mostrar os dados do usuário)
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("SELECT nome, email FROM contas_curso WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    connection.close()
    return usuario

def atualizar_dados(email_atual): # ATUALIZAR O EMAIL OU O NOME E JOGAR ELES NA FUNÇÃO DE UPDATE DO BANCO DE DADOS
    usuario = buscar_usuario_por_email(email_atual)
    nome = usuario[0]     
    email = usuario[1]     

    print("""Digite qual dado você deseja alterar:
1. Nome
2. Email
3. Voltar para o menu principal""")
    escolha = input("Opção: ").strip()
    while escolha not in ["1", "2", "3"]:
        print("Opção inválida. Tente novamente.")
        escolha = input("Opção: ").strip()

    if escolha == "3":
        print("Voltando para o menu principal.")
        return
    
    elif escolha == "2":
        email = input("Digite o novo email: ").strip()

        if not check_email(email): # checa se o return de check_email é false, ou seja, se o email é inválido
            print("Email inválido! O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR")
            return
    elif escolha == "1":
        nome = input("Digite o novo nome: ").strip()
        while not nome: # checa se o nome é vazio, ou seja, se o return de not nome é true
            print("Nome não pode ser vazio.")
            nome = input("Digite o novo nome: ").strip()

    atualizar_dados_banco(email_atual, email, nome) # joga os dados atualizados na função de update do banco de dados

    usuario = buscar_usuario_por_email(email) # mostra os dados atualizados
    print("\n CONFIRA SEUS DADOS ATUALIZADOS:")
    print(f"  Nome:  {usuario[0]}")
    print(f"  Email: {usuario[1]}")
    print("="*50)


def atualizar_dados_banco(email_atual, novo_email, novo_nome): # Update do banco de dados (U do CRUD)
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE contas_curso SET nome = ?, email = ? WHERE email = ?", (novo_nome, novo_email, email_atual))
    connection.commit()
    connection.close()
    print("Dados atualizados com sucesso!")

