import re
import sqlite3
from utils import *
from checagem import *
from time import sleep

def menu_inicial():
    print("\033[1;36m=\033[0m"*50)
    print("\033[1;36m|                👾​COURSEPATH🤖​                  |\033[0m")      
    print("\033[1;36m=\033[0m"*50)
    print("""| Escolha:                                       |
|    \033[1;34m[1]\033[0m. Cadastrar-se                           |
|    \033[1;34m[2]\033[0m. Login                                  |
|    \033[1;34m[3]\033[0m. Sair                                   |
\033[1;36m==================================================\033[0m""")                                                       
    escolha = input("Opção:").strip()
    while escolha not in ["1", "2", "3"]:
        print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
        escolha = input("Opção:").strip()
    return escolha


def fazer_cadastro(cursor, connection): #Todo o fluxo do cadastro(diminuir linhas da main)
    #fiz primeiramente o código utilizando ifs aninhados, porém após revisar o código com a claude resolvi mudar para a metodologia early return
    while True:
        nome = input("Nome: ").strip()
        checar_nome = check_nome(nome)

        if checar_nome:
            print("\033[1;32mNome válido✅​​!\033[0m")
            limpar_tela()
            break
        else:
            print("\033[1;31mNome inválido!❌​ O nome deve conter apenas letras e espaços.​\033[0m")
            sleep(2)
            limpar_tela()
        
    while True:
        email = input("Email (Precisa seguir o formato NOME.SOBRENOME@UFRPE.BR): ").strip().lower()
        if check_email(email):
            print("\033[1;32mEmail válido✅​​!\033[0m")
            sleep(2)
            limpar_tela()
            break
        else:
            print("\033[1;31mEmail inválido!❌​ O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR\033[0m")
            sleep(2)
            limpar_tela()
            
    while True:
        senha = input("Senha: ").strip()
        if check_senha(senha):
            print("\033[1;32mSenha válida✅!\033[0m")
            repetir_senha = input("Repita a senha:").strip()
            if senha == repetir_senha:
                print("\033[1;32mAs senhas coincidem✅!\033[0m")
                break
            else:
                print("\033[1;31mAs senhas não coincidem.❌​\033[0m")
                sleep(2)       
        else:
            print("\033[1;31mSenha inválida!❌​ A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.\033[0m")
            sleep(2)
            limpar_tela()
    

    if not cadastrar_usuario(nome, email, senha):
        print("\033[1;31mErro ao cadastrar usuário.❌​\033[0m")
        return
# Aqui termina o cadastro e inicia o U do CRUD, onde o usuário pode atualizar seus dados cadastrados
    while True:
        sleep(2)
        print("\033[1;32mCadastro realizado com sucesso!✅​\033[0m")
        sleep(2)
        limpar_tela()
        usuario = buscar_usuario_por_email(email)
        print("\n CONFIRA SEUS DADOS CADASTRADOS:")
        print(f"  Nome:  {usuario[0]}")
        print(f"  Email: {usuario[1]}")
        print("="*50)
        print("""Deseja alterar algum dado cadastrado?
        [1]. Sim
        [2]. Não (Sair e fazer login)""")
        if input("Opção: ").strip() == "2":
            print("Faça login para acessar sua conta.")
            break
        atualizar_dados(email)        
        limpar_tela()   

        
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
        print("\033[1;31mErro: Email já cadastrado.❌​\033[0m")
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
[1]. Nome
[2]. Email
[3]. Voltar para o menu principal""")
    escolha = input("Opção: ").strip()
    while escolha not in ["1", "2", "3"]:
        print("\033[1;31mOpção inválida.❌​ Tente novamente.\033[0m")
        escolha = input("Opção: ").strip()

    if escolha == "3":
        print("\033[1;33mVoltando para o menu principal.🔄​\033[0m")
        return
    
    elif escolha == "2":
        email = input("Digite o novo email: ").strip()

        if not check_email(email): # checa se o return de check_email é false, ou seja, se o email é inválido
            print("\033[1;31mEmail inválido!❌​ O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR\033[0m")
            return
    elif escolha == "1":
        nome = input("Digite o novo nome: ").strip()
        while not nome: # checa se o nome é vazio, ou seja, se o return de not nome é true
            print("\033[1;31mNome não pode ser vazio.❌​\033[0m")
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
    print("\033[1;32mDados atualizados com sucesso✅​!\033[0m")

