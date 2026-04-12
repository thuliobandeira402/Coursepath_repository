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
