from others.utils import *
from time import sleep
from menus.menucadeiras01 import *
from menus.menucadeiras02 import *
from cadeiras.cadeirasperiodo2 import *
def semestres_menu():
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*78)
            print("\033[1;36m|                               SEMESTRES                                    |\033[0m")
            print("\033[1;36m=\033[0m"*78) 
            print("""Digite o número do semestre para ver as disciplinas correspondentes:
\033[1;34m[1]\033[0m. 1º Semestre
\033[1;34m[2]\033[0m. 2º Semestre
\033[1;34m[3]\033[0m. 3 Sair""")
        imprimir_cabecalho()
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = cadeiras_menu01()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = cadeiras_menu02()
            if menu == 'menu_principal':
                return 'menu_principal'

        elif escolha == "3":
            print("\033[1;33mVoltando para o menu de cursos...🔄​\033[0m")
            sleep(2)
            limpar_tela() 
            break




