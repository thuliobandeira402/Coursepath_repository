from cadastro import *
import sqlite3
from utils import *
from checagem import *
from menuprincipal import *
from recoverypassword import *

def login(cursor, connection):
    """Função para realizar o login do usuário. Solicita email e senha, verifica as credenciais no banco de dados e 
    direciona para o menu principal se o login for bem-sucedido. Caso contrário, oferece a opção de recuperar a senha."""
    while True:
        while True:
            email = input("Digite seu Email cadastrado: ").strip().lower()
            if check_email(email) == True:
                break
            else: 
                print("\033[1;31mEmail inválido❌​. Certifique-se de usar o formato NOME.SOBRENOME@UFRPE.BR\033[0m")
        while True:
            senha = input("Digite sua Senha: ").strip()
            if check_senha(senha) == True:
                break
            else: 
                print("\033[1;31mSenha inválida❌​. A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.\033[0m")
                forgot_password = input("Esqueci minha senha. Deseja recuperar? (s/n): ").strip().lower()
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
            forgot_password = input("Esqueci minha senha. Deseja recuperar? (s/n): ").strip().lower()
            if forgot_password == 's': 
                recuperar_senha(email)
            sleep(2)
            connection.close()  
            limpar_tela()        
    connection.close()
    

