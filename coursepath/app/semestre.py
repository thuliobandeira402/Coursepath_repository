from utils import *
from tradutor import *
from time import sleep
from menucadeiras import *

def semestres_menu():
    while True:
        print("\033[1;36m=\033[0m"*78)
        print("\033[1;36m|                               SEMESTRES                                    |\033[0m")
        print("\033[1;36m=\033[0m"*78)
        print("""Digite o número do semestre para ver as disciplinas correspondentes:
\033[1;34m[1]\033[0m. 1º Semestre
\033[1;34m[2]\033[0m. 2º Semestre
\033[1;34m[3]\033[0m. 3 Sair""")
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            cadeiras_menu01()
        elif escolha == "2":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            cadeiras_menu02()

        elif escolha == "3":
            print("Voltando para o menu de cursos...🔄​")
            sleep(2)
            limpar_tela() 
            break

def cadeiras_menu01():
    while True:
        print("\033[1;36m=\033[0m"*78)
        print("\033[1;36m|                               CADEIRAS                                     |\033[0m")
        print("\033[1;36m=\033[0m"*78)
        print("""Digite o número da cadeira para ver as disciplinas correspondentes:
\033[1;34m[1]\033[0m. 1 Projeto Interdisciplinar
\033[1;34m[2]\033[0m. 2 Fundamentos Matemáticos
\033[1;34m[3]\033[0m. 3 Principios De Programação
\033[1;34m[4]\033[0m. 4 Sustentabilidade e Sistemas de Informação
\033[1;34m[5]\033[0m. 5 Introdução a Sistemas de Administração
\033[1;34m[6]\033[0m. 6 Sair""")
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4", "5", "6"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            projeto_interdisciplinar_menu()
        elif escolha == "2":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            fundamentos_matematicos01_menu()
        elif escolha == "3":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela() 
            principios_de_programacao_menu()
        elif escolha == "4":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            sustentabilidade_e_sistemas_de_informacao_menu()       
        elif escolha == "5":    
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            introducao_a_sistemas_de_administracao_menu()
        elif escolha == "6":
            print("Voltando para o menu de semestres...🔄​")
            sleep(2)
            limpar_tela()
            break

def cadeiras_menu02():
    while True:
        print("\033[1;36m=\033[0m"*78)
        print("\033[1;36m|                               CADEIRAS                                     |\033[0m")
        print("\033[1;36m=\033[0m"*78)
        print("""Digite o número da cadeira para ver as disciplinas correspondentes:
\033[1;34m[1]\033[0m. 1 Projeto Interdisciplinar 02
\033[1;34m[2]\033[0m. 2 Fundamentos Matemáticos 02
\033[1;34m[3]\033[0m. 3 Fundamentos De Problemas Computacionais
\033[1;34m[4]\033[0m. 4 Elementos De Sistemas Computacionais
\033[1;34m[5]\033[0m. 5 Fundamentos De Sistemas De Informação
\033[1;34m[6]\033[0m. 6 Sair""")
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4", "5", "6"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            projeto_interdisciplinar02_menu()
        elif escolha == "2":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            fundamentos_matematicos02_menu()
        elif escolha == "3":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela() 
            fundamentos_de_problemas_computacionais_menu()
        elif escolha == "4":
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()   
            elementos_de_sistemas_computacionais_menu()    
        elif escolha == "5":    
            print("CARREGANDO...🔄​")
            sleep(2)
            limpar_tela()
            fundamentos_de_sistemas_de_informacao_menu()
        elif escolha == "6":
            print("Voltando para o menu de semestres...🔄​")
            sleep(2)
            limpar_tela()
            break

