from sqlite.database import *
from user.update_fluxo import atualizar_dados
from others.utils import limpar_tela
def read_cadastro(email_atual):
    """Função de read que será chamada após o cadastro"""
    email = email_atual
    usuario = buscar_usuario_por_email(email_atual)

    while True: 
        usuario = buscar_usuario_por_email(email)
        if usuario is None:
            print("\033[1;31mErro: usuário não encontrado após cadastro.❌\033[0m")
            sleep(2)
            return
        def print_dados_usuario():
            print("\033[1;36m=\033[0m"*50)
            print("|         \033[1;36mCONFIRA SEUS DADOS CADASTRADOS:        |\033[0m")
            print("\033[1;36m=\033[0m"*50)
            print(f"  \033[1;34mNome:\033[0m  {usuario[0]}")
            print(f"  \033[1;34mEmail:\033[0m {usuario[1]}")
            print("\033[1;36m=\033[0m"*50)
            print("""Deseja alterar algum dado cadastrado?
            \033[1;34m[1]\033[0m. Sim
            \033[1;34m[2]\033[0m. Não (Sair e fazer login)""")
            print("\033[1;36m=\033[0m"*50)
        print_dados_usuario()
        escolha = input("Opção: ").strip()
        while escolha not in ["1","2"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            sleep(2)
            limpar_tela()
            print_dados_usuario()
            escolha = input("Opção:").strip()
        if escolha == "2":
            print("\033[1;33mFaça login para acessar sua conta.\033[0m")
            sleep(2)
            return
        sleep(2)
        limpar_tela()
        email = atualizar_dados(email)        
        limpar_tela() 