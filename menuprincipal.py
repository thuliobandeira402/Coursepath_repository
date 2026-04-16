from utils import *
from time import sleep
from cursos import *
from userconfig import *


def menu_principal(cursor, connection, user_id):
    while True:
        print("-"*50)
        print("Bem-vindo ao Menu Principal!")
        print("-"*50)
        print("""1. Ver Cursos Disponíveis
2. Alterar idioma do menu de cursos
3. Alterar dados do usuário
4. Sair""")
        escolha = input("Digite o número da opção desejada: ").strip()
        while escolha not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida. Tente novamente.")
            escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            limpar_tela()
            menu_cursos()
        elif escolha == "2":
            print("Prosseguindo para o menu de idiomas...")
            sleep(2)
            limpar_tela()
            menu_idiomas()
        elif escolha == "3":
            print("Prosseguindo para o menu de configurações do usuário...")
            sleep(2)
            limpar_tela()
            menu_config(cursor, connection, user_id)   
        elif escolha == "4":
            print("Voltando ao menu inicial...")
            sleep(2)
            limpar_tela()
            break