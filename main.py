from cadastro import *
from login import *
from utils import *
def main():
    while True:
        limpar_tela()
        criar_tabela()
        escolha = menu_inicial()
        if escolha == "1": #cadastramento do usuário
            limpar_tela()
            sleep(1)
            fazer_cadastro()
        elif escolha == "2":
            print("Prosseguindo para o login...")
            sleep(2)
            limpar_tela()
            login()
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            sleep(2)
            limpar_tela()
            break
if __name__ == "__main__":
    main()