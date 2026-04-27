from others.utils import *
from user.cadastro import *
from verifications.checagem_email_senha_nome import *
from time import sleep
import sqlite3


def menu_config(cursor, connection, user_id):
    while True:
        def imprimir_menu():
            print("\033[1;36m=\033[0m"*50)
            print("\033[1;36m|            Configurações do Usuário            |\033[0m")
            print("\033[1;36m=\033[0m"*50)
            print("""\033[1;34m[1].\033[0m Alterar nome
\033[1;34m[2].\033[0m Alterar email
\033[1;34m[3].\033[0m Alterar senha
\033[1;34m[4].\033[0m Deletar conta
\033[1;34m[5].\033[0m Voltar ao menu principal""")
        imprimir_menu()
        escolha = input("Digite o número da opção desejada: ").strip()
        while escolha not in ["1", "2", "3", "4", "5"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_menu()
            escolha = input("Digite o número da opção desejada: ").strip()
        if escolha == "1":
            while True:
                novo_nome = input("Digite o novo nome: ").strip()
                if check_nome(novo_nome):
                    print("\033[1;32mNome válido!✅​\033[0m")
                    cursor.execute("UPDATE contas_curso SET nome = ? WHERE id = ?", (novo_nome, user_id))
                    connection.commit()
                    sleep(1)
                    print("\033[1;32mNome atualizado com sucesso!✅​\033[0m")
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    print("\033[1;31mNome inválido! O nome deve conter apenas letras e espaços.❌​\033[0m")
                    sleep(2)
                    limpar_tela()
        elif escolha == "2":
            while True:
                novo_email = input("Digite o novo email: ").strip().lower()
                if check_email(novo_email):
                    print("\033[1;32mEmail válido!✅​\033[0m")
                    cursor.execute("UPDATE contas_curso SET email = ? WHERE id = ?", (novo_email, user_id))
                    connection.commit()
                    sleep(1)
                    print("\033[1;32mEmail atualizado com sucesso!✅​\033[0m")
                    sleep(2)
                    limpar_tela()
                    break
                else:
                    print("\033[1;31mEmail inválido! O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR❌​\033[0m")
                    sleep(2)
                    limpar_tela()
        elif escolha == "3":
            while True:
                nova_senha = input("Digite a nova senha: ").strip()
                if check_senha(nova_senha):
                    print("\033[1;32mSenha válida!✅​\033[0m")
                    repetir_senha = input("Repita a nova senha: ").strip()
                    if nova_senha == repetir_senha:
                        print("\033[1;32mAs senhas coincidem!✅​\033[0m")
                        cursor.execute("UPDATE contas_curso SET senha = ? WHERE id = ?", (nova_senha, user_id))
                        connection.commit()
    
                        sleep(1)
                        print("\033[1;32mSenha atualizada com sucesso!✅​\033[0m")
                        sleep(2)
                        limpar_tela()
                        break
                    else:
                        print("\033[1;31mAs senhas não coincidem.❌​\033[0m")
                else:
                    print("\033[1;31mSenha inválida! A senha deve conter no mínimo 8 caracteres, incluindo letras maiúsculas, minúsculas e números.❌​\033[0m")
                    sleep(2)
                    limpar_tela()
        elif escolha == "4":
            confirmacao = input("Tem certeza que deseja deletar sua conta? Esta ação é irreversível. (S/N): ").strip().upper()
            if confirmacao == "S":
                cursor.execute("DELETE FROM contas_curso WHERE id = ?", (user_id,))
                connection.commit()
                print("\033[1;32mConta deletada com sucesso. Voltando ao menu inicial...✅​\033[0m")
                sleep(2)
                limpar_tela()
                break
            else:
                print("\033[1;33mAção cancelada. Voltando ao menu de configurações...🔄​\033[0m")
                sleep(2)
                limpar_tela()
        elif escolha == "5":
            print("\033[1;33mVoltando ao menu principal...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break