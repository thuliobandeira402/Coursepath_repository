from utils import *
from time import sleep
from menubsi import *
from deep_translator import GoogleTranslator
from tradutor import *


def menu_cursos():
    while True:
        print("\033[1;36m=\033[0m"*54)
        print("\033[1;36m|                 Cursos Disponíveis                 |\033[0m")
        print("\033[1;36m=\033[0m"*54)
        print("""\033[1;34m[1]\033[0m. BSI - Bacharelado em Sistemas de Informação
\033[1;34m[2]\033[0m. BCC - Bacharelado em Ciência da Computação(em breve)
\033[1;34m[3]\033[0m. para voltar ao menu principal""")
        escolha = input("Digite o número do curso desejado: ").strip().upper()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            escolha = input("Digite o número do curso desejado: ").strip().upper()
        if escolha == "1":
            print("\033[1;33mCarregando informações do curso de BSI...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            bsi()
        elif escolha == "2":
            print("\033[1;33mA ser desenvolvido...🔄​\033[0m")
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            print("\033[1;33mVoltando ao menu principal.🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def menu_idiomas():
    while True:
        print("\033[1;36m=\033[0m"*50)
        print("\033[1;36m|            Configurações de Idioma             |\033[0m")
        print("\033[1;36m=\033[0m"*50)
        change_language()
        limpar_tela()
        break
