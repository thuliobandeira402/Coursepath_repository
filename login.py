from cadastro import *
import sqlite3
from utils import *
from checagem import *
from menuprincipal import *
from recoverypassword import *

def login():
    """Função para realizar o login do usuário. Solicita email e senha, verifica as credenciais no banco de dados e 
    direciona para o menu principal se o login for bem-sucedido. Caso contrário, oferece a opção de recuperar a senha."""
    while True:
        while True:
            email = input("Digite seu Email cadastrado: ").strip().lower()
            if check_email(email) == True:
                break
            else: 
                print("Email inválido. Certifique-se de usar o formato NOME.SOBRENOME@UFRPE.BR")
        while True:
            senha = input("Digite sua Senha: ").strip()
            if check_senha(senha) == True:
                break
            else: 
                print("Senha inválida. A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
                forgot_password = input("Esqueci minha senha. Deseja recuperar? (s/n): ").strip().lower()
                if forgot_password == 's': 
                    recuperar_senha(email)
                    break
        
        connection = sqlite3.connect('banco.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM contas_curso WHERE email = ? AND senha = ?", (email, senha))
        usuario = cursor.fetchone()
        
        if usuario:
            print("Login bem-sucedido! Proseguindo para o menu principal...")
            sleep(2)
            limpar_tela()
            menu_principal()
            break
        else:
            print("Email ou senha incorretos. Tente novamente.")
            forgot_password = input("Esqueci minha senha. Deseja recuperar? (s/n): ").strip().lower()
            if forgot_password == 's': 
                recuperar_senha(email)
            sleep(2)
            connection.close()  
            limpar_tela()        
    connection.close()
    

