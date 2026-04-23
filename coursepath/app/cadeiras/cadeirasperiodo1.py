from others.utils import *
from time import sleep
from menus.menucadeiras import *
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