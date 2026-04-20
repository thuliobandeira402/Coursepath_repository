from utils import *
from time import sleep
import sqlite3

"""Nesse arquivo ficarão todas as funções que envolvam banco de dados"""

def criar_tabela(): 
    """Criar tabela de usuários para cadastro no banco de dados"""
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


def cadastrar_usuario(nome, email, senha):
    """Tenta colocar os dados dos usuários no banco de dados, caso o email já esteja cadastrado
    o erro é exibido"""
    connection = sqlite3.connect('banco.db') 
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO contas_curso (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        connection.commit()
        connection.close()
        return True
    except sqlite3.IntegrityError:
        connection.close()
        print("\033[1;31mErro: Email já cadastrado.❌​\033[0m")
        return False
    

def buscar_usuario_por_email(email): 
    """Buscar por algum usuario no banco de dados utilizando seu email"""


    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("SELECT nome, email FROM contas_curso WHERE email = ?", (email,))
    usuario = cursor.fetchone()

    return usuario


def atualizar_dados_banco(email_atual, novo_email, novo_nome):
    """Update do banco de dados (U do CRUD) """


    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE contas_curso SET nome = ?, email = ? WHERE email = ?", (novo_nome, novo_email, email_atual))
    connection.commit()
 
    print("\033[1;32mDados atualizados com sucesso✅​!\033[0m")
    sleep(2)
    return novo_email


