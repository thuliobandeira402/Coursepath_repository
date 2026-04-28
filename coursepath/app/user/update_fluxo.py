from verifications.checagem_email_senha_nome import *
from others.utils import *
from time import sleep
from sqlite.database import *

""""Fluxo do UPDATE"""

def atualizar_dados(email_atual):
    """ATUALIZAR O EMAIL OU O NOME E JOGAR ELES NA FUNÇÃO DE UPDATE DO BANCO DE DADOS"""
    usuario = buscar_usuario_por_email(email_atual)
    nome = usuario[0]     
    email = usuario[1]     
    def imprimir_cabecalho():
        print("""\033[1;34mDigite qual dado você deseja alterar:
[1]. Nome
[2]. Email
[3]. Voltar""")
    imprimir_cabecalho()
    escolha = input("Opção: ").strip()
    while escolha not in ["1", "2", "3"]:
        print("\033[1;31mOpção inválida.❌​ Tente novamente.\033[0m")
        sleep(2)
        limpar_tela()
        imprimir_cabecalho()
        escolha = input("Opção: ").strip()
    

    if escolha == "3":
        print("\033[1;33mVoltando para o menu principal.🔄​\033[0m")
        sleep(2)
        return
    
    elif escolha == "2":
        email = input("Digite o novo email: ").strip()

        if not check_email(email): # checa se o return de check_email é false, ou seja, se o email é inválido
            print("\033[1;31mEmail inválido!❌​ O email deve seguir o formato: NOME.SOBRENOME@UFRPE.BR\033[0m")
            sleep(2)
            return

    elif escolha == "1":
        nome = input("Digite o novo nome: ").strip()
        while not nome: # checa se o nome é vazio, ou seja, se o return de not nome é true
            print("\033[1;31mNome não pode ser vazio.❌​\033[0m")
            sleep(2)
            limpar_tela()
            nome = input("Digite o novo nome: ").strip()

    novos_dados = atualizar_dados_banco(email_atual, email, nome)
    return novos_dados
    # joga os dados atualizados na função de update do banco de dados

#fim do update, declararei a função de read abaixo para facilitar correções

