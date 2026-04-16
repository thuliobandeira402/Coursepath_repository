from utils import *
from cadastro import *
from checagem import *
from time import sleep
import sqlite3


def menu_config(cursor, connection, user_id):
    while True:
        print("-"*50)
        print("Configurações do Usuário")
        print("-"*50)
        print("""1. Alterar nome
2. Alterar email
3. Alterar senha
4. Deletar conta
5. Voltar ao menu principal""")
        escolha = input("Digite o número da opção desejada: ").strip()
        while escolha not in ["1", "2", "3", "4", "5"]:
            print("Opção inválida. Tente novamente.")
            escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if check_nome(novo_nome):
                    print("Nome válido!")
                    cursor.execute("UPDATE contas_curso SET nome = ? WHERE id = ?", (novo_nome, user_id))
                    connection.commit()
                    sleep(1)
                    print("Nome atualizado com sucesso!")
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    print("Nome inválido! O nome deve conter apenas letras e espaços.")
                    sleep(2)
                    limpar_tela()
        elif escolha == "2":
            while True:
                novo_email = input("Digite o novo email: ").strip().lower()
                if check_email(novo_email):
                    print("Email válido!")
                    cursor.execute("UPDATE contas_curso SET email = ? WHERE id = ?", (novo_email, user_id))
                    connection.commit()
                    sleep(1)
                    print("Email atualizado com sucesso!")
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    print("Email inválido! O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR")
                    sleep(2)
                    limpar_tela()
        elif escolha == "3":
            while True:
                nova_senha = input("Digite a nova senha: ").strip()
                if check_senha(nova_senha):
                    print("Senha válida!")
                    repetir_senha = input("Repita a nova senha: ").strip()
                    if nova_senha == repetir_senha:
                        print("As senhas coincidem.")
                        cursor.execute("UPDATE contas_curso SET senha = ? WHERE id = ?", (nova_senha, user_id))
                        connection.commit()
    
                        sleep(1)
                        print("Senha atualizada com sucesso!")
                        sleep(2)
                        limpar_tela()
                        break
                    else:
                        print("As senhas não coincidem.")
                else:
                    print("Senha inválida! A senha deve conter no mínimo 8 caracteres, incluindo letras maiúsculas, minúsculas e números.")
                    sleep(2)
                    limpar_tela()
        elif escolha == "4":
            confirmacao = input("Tem certeza que deseja deletar sua conta? Esta ação é irreversível. (S/N): ").strip().upper()
            if confirmacao == "S":
                cursor.execute("DELETE FROM contas_curso WHERE id = ?", (user_id,))
                connection.commit()
                print("Conta deletada com sucesso. Voltando ao menu inicial...")
                sleep(2)
                limpar_tela()
                break
            else:
                print("Ação cancelada. Voltando ao menu de configurações...")
                sleep(2)
                limpar_tela()
        elif escolha == "5":
            print("Voltando ao menu principal...")
            sleep(2)
            limpar_tela()
            break