from others.utils import *
from time import sleep
from menus.menubsi import *
from deep_translator import GoogleTranslator
from others.tradutor import *


def menu_cursos():
    while True:
        def imprimir_cabecalho():
            """Função para reimprimir o cabeçalho do menu após uma opção inválida."""
            print("\033[1;36m=\033[0m"*54)
            print("\033[1;36m|                 Cursos Disponíveis                 |\033[0m")
            print("\033[1;36m=\033[0m"*54)
            print("""\033[1;34m[1]\033[0m. BSI - Bacharelado em Sistemas de Informação
\033[1;34m[2]\033[0m. BCC - Bacharelado em Ciência da Computação(em breve)
\033[1;34m[3]\033[0m. para voltar ao menu principal""")
        imprimir_cabecalho()
        escolha = input("Digite o número do curso desejado: ").strip().upper()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            escolha = input("Digite o número do curso desejado: ").strip().upper()
        if escolha == "1":
            print("\033[1;33mCarregando informações do curso de BSI...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = bsi()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mA ser desenvolvido...🔄​\033[0m")
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            print("\033[1;33mVoltando ao menu principal.🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break

        


