from utils import *
from tradutor import *
import textwrap
from time import sleep
INTRODUCTION_TEXT = ("""O objetivo principal do curso de Bacharelado em Sistemas de Informação é formar 
profissionais munidos de conhecimentos técnicos e científicos, para o desenvolvimento de sistemas de informação
intensivos em software nas mais variadas complexidades. O egresso será capaz de projetar, implantar, gerenciar
e inovar processos envolvendo sistemas de informação pararesolver problemas das organizações, governo, sociedade
e modificar o contexto sócio-político-econômico-científico no qual se encontra.""")


def bsi():
    in_portuguese = False
    while True:
        print("\033[1;36m=\033[0m"*78)
        print("\033[1;36m|                                    BSI                                     |\033[0m")
        print("\033[1;36m=\033[0m"*78)
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*78)
        variable_options(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mA ser desenvolvido...🔄​\033[0m")
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("Voltando para o menu de cursos...🔄​")
            sleep(2)
            limpar_tela()
            break
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
