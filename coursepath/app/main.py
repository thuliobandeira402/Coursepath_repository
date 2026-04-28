from user.cadastro import fazer_cadastro
from user.login import *
from others.utils import *
from sqlite.database import *
from menus.menuinicial import *
from time import sleep
connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

def main():
    while True:
        limpar_tela()
        criar_tabela()
        menu_inicial()
        escolha = input("Opção:").strip()
        while escolha not in ["1", "2", "3"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            sleep(2)
            limpar_tela()
            menu_inicial()
            escolha = input("Opção:").strip()
        if escolha == "1": #cadastramento do usuário
            limpar_tela()
            sleep(2)
            fazer_cadastro(cursor, connection)
        elif escolha == "2": #login do usuário 
            print("\033[1;33mProsseguindo para o login...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            login(cursor, connection)
        elif escolha == "3": #sair do programa
            print("\033[1;33mSaindo do programa. Até logo!🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break
if __name__ == "__main__":
    main()



