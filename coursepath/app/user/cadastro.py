from others.utils import limpar_tela
from verifications.checagem_email_senha_nome import *
from time import sleep
from sqlite.database import *
from user.read import read_cadastro


def fazer_cadastro(cursor, connection): 
    """Fluxo do cadastro organizado"""
    while True: # inserir nome
        nome = input("\033[1;33mNome: \033[0m").strip()
        checar_nome = check_nome(nome)
        if checar_nome:
            print("\033[1;32mNome válido✅​​!\033[0m")
            sleep(2)
            limpar_tela()
            break
        else:
            print("\033[1;31mNome inválido!❌​ O nome deve conter apenas letras e espaços.​\033[0m")
            sleep(2)
            limpar_tela()
        
    while True: # inserir email
        email = input("\033[1;33mEmail (Precisa seguir o formato NOME.SOBRENOME@UFRPE.BR): \033[0m").strip().lower()
        if check_email(email):
            if not check_email_existe(email):
                print("\033[1;32mEmail válido✅​​!\033[0m")
                sleep(2)
                limpar_tela()
                break
            else:
                print("\033[1;31mEmail já cadastrado!❌​\033[0m")
                sleep(2)
                limpar_tela()
                return
        else:
            print("\033[1;31mEmail inválido!❌​ O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR\033[0m")
            sleep(2)
            limpar_tela()
            
    while True: #inserir senha
        senha = input("\033[1;33mSenha: \033[0m").strip()
        if check_senha(senha):
            print("\033[1;32mSenha válida✅!\033[0m")
            repetir_senha = input("\033[1;33mRepita a senha: \033[0m").strip()
            if senha == repetir_senha:
                print("\033[1;32mAs senhas coincidem✅!\033[0m")
                sleep(2)
                break
            else:
                print("\033[1;31mAs senhas não coincidem.❌​\033[0m")
                sleep(2)
                limpar_tela()      
        else:
            print("\033[1;31mSenha inválida!❌​ A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.\033[0m")
            sleep(2)
            limpar_tela()
    

    if not cadastrar_usuario(nome, email, senha): #Essa chamada tenta cadastrar o usuário, se falhar exibe erro
        print("\033[1;31mErro ao cadastrar usuário.❌​\033[0m")
        sleep(2)
        return
    print("\033[1;32mCadastro realizado com sucesso!✅​\033[0m")
    sleep(2)
    limpar_tela()
    # Aqui termina o cadastro e os dados são mostrados para o usuário conferir se estão corretos
    read_cadastro(email)   
    #fim do cadastro
        

    




