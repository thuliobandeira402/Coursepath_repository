from cadastro import *
import sqlite3
import utils
import checagem
from menuprincipal import *
def login():
    email = input("Digite seu Email cadastrado: ").strip().lower()
    senha = input("Digite sua Senha: ").strip()
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contas_curso WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()
    
    if usuario:  
        print("Login bem-sucedido! Proseguindo para o menu principal...")
        sleep(2)
        limpar_tela()
        menu_principal()
    else:
        print("Email ou senha incorretos. Tente novamente.")
        connection.close()  
        menu_inicial()  
          
    connection.close()

