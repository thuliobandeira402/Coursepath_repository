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
        print("\n CONFIRA SEUS DADOS CADASTRADOS:")
        print(f"  Nome:  {usuario[0]}")
        print(f"  Email: {usuario[1]}")
        print("="*50)
        print("""Deseja alterar algum dado cadastrado?
        [1]. Sim
        [2]. Não (Sair e fazer login)""")
        escolha = input("Opção: ").strip()
        while escolha not in ["1","2"]:
            print("\033[1;31mOpção inválida. Tente novamente.❌​\033[0m")
            escolha = input("Opção:").strip()
        if escolha == "2":
            print("Faça login para acessar sua conta.")
            sleep(2)
            return
        sleep(2)
        limpar_tela()
        email = atualizar_dados(email)        
        limpar_tela() 