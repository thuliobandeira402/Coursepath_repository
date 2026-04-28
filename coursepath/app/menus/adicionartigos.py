
from others.utils import *
from time import sleep
from deep_translator import GoogleTranslator
from others.tradutor import *
from menus.menuprincipal import *
from others.utils import variable_options_addarticle





def menu_adicionar_artigo(cursor, connection, user_id):
    while True:
        print("\033[1;36m=\033[0m"*50)
        print("\033[1;36m|                ADICIONAR ARTIGO                |\033[0m")
        print("\033[1;36m=\033[0m"*50) 
        titulo = input("Digite o título do artigo que deseja adicionar: ")
        abstract = input("Cole o abstract aqui: ").strip()
        sleep(1)
        limpar_tela()
        in_portuguese = False
        while True:
            if in_portuguese:
                traducao = abstract
                traducao_titulo = titulo
            else:
                traducao_titulo = translating_text(titulo)
                traducao = translating_text(abstract)
            def imprimir_cabecalho():
                """Criei essa função para reimprimir o cabeçalho do menu, pois quando o usuário digita
                uma opção inválida, o menu é limpo e reexibido, mas o cabeçalho não é reimpresso, então essa função
                serve para corrigir isso"""
                print("\033[1;36m=\033[0m"*50)
                print("\033[1;36m|                ADICIONAR ARTIGO                |\033[0m")
                print("\033[1;36m=\033[0m"*50) 
                print(f"título do artigo adicionado: \033[1;32m{traducao_titulo}\033[0m")
                print("\n\033[1;33mTradução do abstract:\033[0m")
                print(f"\033[1;32m{traducao}\033[0m")   
                print("\033[1;36m=\033[0m"*50)
            imprimir_cabecalho()
            variable_options_addarticle(in_portuguese)
            escolha = input("Digite o número da opção desejada: ").strip()
            while escolha not in ["1", "2", "3"]:
                print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
                sleep(2)
                limpar_tela()
                imprimir_cabecalho()
                variable_options_addarticle(in_portuguese)
                escolha = input("Digite o número da opção desejada: ").strip()
            if escolha == "1":
                change_language()
                sleep(2)
                limpar_tela()
            elif in_portuguese and escolha == "2":
                    in_portuguese = False
                    sleep(1)
                    limpar_tela()
            elif escolha == "2":
                in_portuguese = True
                sleep(1)
                limpar_tela()  
            elif escolha == "3":
                print("\033[1;33mVoltando ao menu principal...🔄​\033[0m")
                sleep(2)
                limpar_tela()
                return 
            
           
       
