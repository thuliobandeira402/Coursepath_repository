from tradutor import *
from utils import *
from time import sleep

def artigos_01_projeto_interdisciplinar01():
    in_portuguese = False
    while True:
        print("\033[1;36m=\033[0m"*110)
        print("""\033[1;36m|                                   Computação: O vetor de transformação da sociedade
                                                Autores: Avelino Francisco Zorzo, Andree Luis Alice Raabe, Christian Brackmann|\033[0m""")
        print("\033[1;36m=\033[0m"*110)
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_PROJETOINTERDISCIPLINAR01, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_PROJETOINTERDISCIPLINAR01)
            formatted = textwrap.fill(translated, width=80)
            print(formatted)
        print("\033[1;36m=\033[0m"*110)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
        elif escolha == "2":
            print("Voltando para o menu de cadeiras...🔄​")
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
        elif escolha == "4":
            print("Voltando para o menu de cadeiras...🔄​" )
            sleep(2)
            limpar_tela()
            break