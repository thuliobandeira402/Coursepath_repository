from time import sleep
import sqlite3
from others.utils import limpar_tela
from verifications.checagem_email_senha_nome import *
from menus.menuprincipal import menu_principal
from user.recoverypassword import *
from sqlite.database import check_email_existe

def login(cursor, connection):
    """Função para realizar o login do usuário. Solicita email e senha, verifica as credenciais no banco de dados e 
    direciona para o menu principal se o login for bem-sucedido. Caso contrário, oferece a opção de recuperar a senha."""
    while True:
        while True:
            email = input("\033[1;33mDigite seu Email cadastrado: \033[0m").strip().lower()
            if check_email(email) == True:
                if not check_email_existe(email):
                    print("\033[1;31mEmail não encontrado❌​. Verifique se você digitou corretamente ou se já possui uma conta.\033[0m")
                    sleep(2)
                    limpar_tela()
                    return
                break
            else: 
                print("\033[1;31mEmail inválido❌​. Certifique-se de usar o formato NOME.SOBRENOME@UFRPE.BR\033[0m")
                sleep(2)
                limpar_tela()
        while True:
            senha = input("\033[1;33mDigite sua Senha: \033[0m").strip()
            if check_senha(senha) == True:
                break
            else: 
                print("\033[1;31mSenha inválida❌​. A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.\033[0m")
                sleep(2)
                limpar_tela()
                forgot_password = input("\033[1;33mEsqueci minha senha. Deseja recuperar?\033[0m (\033[1;34ms\033[0m/\033[1;31mn\033[0m): ").strip().lower()
                if forgot_password == 's': 
                    recuperar_senha(email)
                    break
        
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contas_curso WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        
        if usuario:
            print("\033[1;32mLogin bem-sucedido!✅​ Proseguindo...")
            user_id = usuario[0]  # Supondo que o ID do usuário seja a primeira coluna para o menu principal...\033[0m")
            sleep(2)
            limpar_tela()
            menu_principal(cursor, connection, user_id)
            break
        else:
            print("\033[1;31mEmail ou senha incorretos❌​. Tente novamente.\033[0m")
            sleep(2)
            limpar_tela()
            forgot_password = input("\033[1;33mEsqueci minha senha. Deseja recuperar? (s/n): \033[0m").strip().lower()
            if forgot_password == 's': 
                recuperar_senha(email)
            sleep(2)
            connection.close()  
            limpar_tela()        
    connection.close()
    

