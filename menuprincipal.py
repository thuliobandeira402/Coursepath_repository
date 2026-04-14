from utils import *
from time import sleep
from cursos import *
def menu_principal():
    while True:
        print("-"*50)
        print("Bem-vindo ao Menu Principal!")
        print("-"*50)
        print("""1. Ver Cursos Disponíveis
2. Deletar conta
3. Alterar idioma do menu de cursos
4. Sair""")
        escolha = input("Digite o número da opção desejada: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            limpar_tela()
            menu_cursos()
        elif escolha == "2":
            print("A ser desenvolvido...")
        elif escolha == "3":
            print("A ser desenvolvido...")
        elif escolha == "4":
            print("Voltando ao menu inicial...")
            sleep(2)
            limpar_tela()
            break