from others.utils import *
from time import sleep
from menus.menucadeiras import *
from cadeiras.cadeirasperiodo1 import *
from cadeiras.cadeirasperiodo2 import *
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




