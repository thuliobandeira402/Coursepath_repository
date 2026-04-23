from others.utils import *
from time import sleep
from menus.cursos import *
from user.userconfig import *


def menu_principal(cursor, connection, user_id):
    while True:
        print("\033[1;36m=\033[0m"*50)
        print("\033[1;36m|                Menu Principal                  |\033[0m")
        print("\033[1;36m=\033[0m"*50)
        print("""\033[1;34m[1]\033[0m. Ver Cursos Disponíveis
\033[1;34m[2]\033[0m. Alterar idioma do menu de cursos
\033[1;34m[3]\033[0m. Alterar dados do usuário
\033[1;34m[4]\033[0m. Sair""")
        escolha = input("Digite o número da opção desejada: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            limpar_tela()
            menu_cursos()
        elif escolha == "2":
            print("\033[1;33mProsseguindo para o menu de idiomas...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu_idiomas()
        elif escolha == "3":
            print("\033[1;33mProsseguindo para o menu de configuração do usuário...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu_config(cursor, connection, user_id)
        elif escolha == "4":
            print("Voltando ao menu inicial...")
            sleep(2)
            limpar_tela()
            break