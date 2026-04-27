from others.utils import *
from time import sleep
from cadeiras.cadeirasperiodo2 import *
def cadeiras_menu02():
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*78)
            print("\033[1;36m|                               CADEIRAS                                     |\033[0m")
            print("\033[1;36m=\033[0m"*78)
            print("""Digite o número da cadeira para ver as disciplinas correspondentes:
\033[1;34m[1]\033[0m. 1 Projeto Interdisciplinar 02
\033[1;34m[2]\033[0m. 2 Fundamentos Matemáticos 02
\033[1;34m[3]\033[0m. 3 Fundamentos De Problemas Computacionais
\033[1;34m[4]\033[0m. 4 Elementos De Sistemas Computacionais
\033[1;34m[5]\033[0m. 5 Fundamentos De Sistemas De Informação
\033[1;34m[6]\033[0m. 6 Sair
\033[1;34m[7]\033[0m. 7 Voltar para o menu principal""")
        imprimir_cabecalho()
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = projeto_interdisciplinar02_menu()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = fundamentos_matematicos02_menu()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela() 
            menu =  fundamentos_de_problemas_computacionais_menu()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "4":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()   
            menu = elementos_de_sistemas_computacionais_menu()    
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "5":    
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = fundamentos_de_sistemas_de_informacao_menu()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "6":
            print("\033[1;33mVoltando para o menu de semestres...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break
        elif escolha == "7":
            print("\033[1;33mVoltando para o menu principal...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            return 'menu_principal'
