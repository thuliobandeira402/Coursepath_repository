from cadastro import *
from login import *
from utils import *
import sqlite3

def criar_tabela(): #Criar tabela de usuários para cadastro no banco de dados
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS contas_curso (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            senha TEXT NOT NULL
                        )""")
    connection.commit()
    connection.close()

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
            print("Prosseguindo para o login...")
            sleep(2)
            limpar_tela()
            login(cursor, connection)
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            sleep(2)
            limpar_tela()
            break
if __name__ == "__main__":
    main()