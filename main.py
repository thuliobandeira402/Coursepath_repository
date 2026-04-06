from funcoes import *

def main():
    criar_tabela()
    menu_inicial()
    escolha = menu_inicial()
    if escolha == "1": #cadastramento do usuário
        fazer_cadastro()
    elif escolha == "2":
        print("Login ainda não implementado.")

if __name__ == "__main__":
    main()