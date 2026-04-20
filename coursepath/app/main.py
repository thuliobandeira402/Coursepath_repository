from cadastro import *
from login import *
from utils import *
from sqlite3 import *
from database import criar_tabela


connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

def main():
    while True:
        limpar_tela()
        criar_tabela()
        escolha = menu_inicial()
        if escolha == "1": #cadastramento do usuário
            limpar_tela()
            sleep(1)
            fazer_cadastro(cursor, connection)
        elif escolha == "2":
            print("Prosseguindo para o login...🔄​")
            sleep(2)
            limpar_tela()
            login(cursor, connection)
        elif escolha == "3":
            print("Saindo do programa. Até logo!🔄​")
            sleep(2)
            limpar_tela()
            break
if __name__ == "__main__":
    main()



def menu_inicial():
    print("\033[1;36m=\033[0m"*50)
    print("\033[1;36m|                👾​COURSEPATH🤖​                  |\033[0m")      
    print("\033[1;36m=\033[0m"*50)
    print("""| Escolha:                                       |
|    \033[1;34m[1]\033[0m. Cadastrar-se                           |
|    \033[1;34m[2]\033[0m. Login                                  |
|    \033[1;34m[3]\033[0m. Sair                                   |
\033[1;36m==================================================\033[0m""")                                                       
    escolha = input("Opção:").strip()
    while escolha not in ["1", "2", "3"]:
        print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
        escolha = input("Opção:").strip()
    return escolha
