from utils import *
from time import sleep
from menubsi import *
from deep_translator import GoogleTranslator
from tradutor import *


def menu_cursos():
    while True:
        print("-"*50)
        print("Cursos Disponíveis")
        print("-"*50)
        print("""1. BSI - Bacharelado em Sistemas de Informação
2. BCC - Bacharelado em Ciência da Computação(em breve)
V. para voltar ao menu principal""")
        escolha = input("Digite o número do curso desejado: ").strip().upper()
        while escolha not in ["1", "2", "V"]:
            print("Opção inválida. Tente novamente.")
            escolha = input("Digite o número do curso desejado: ").strip().upper()
        if escolha == "1":
            print("Carregando informações do curso de BSI...")
            sleep(2)
            limpar_tela()
            bsi()
        elif escolha == "2":
            print("A ser desenvolvido...")
        elif escolha == "V":
            print("Voltando ao menu principal...")
            sleep(2)
            limpar_tela()
            break


def menu_idiomas():
    while True:
        print("-"*50)
        print("Configurações de Idioma")
        print("-"*50)
        change_language()
        break



