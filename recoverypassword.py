import sqlite3
from checagem import *
from utils import *
def recuperar_senha(email):
    '''Função para recuperar a senha do usuário. Solicita o email do usuário, verifica se o email existe no banco
      de dados e, se existir, permite que o usuário defina uma nova senha. A nova senha deve atender aos critérios 
      de validação definidos na função check_senha. Se o email não for encontrado, exibe uma mensagem de erro.'''
    connection = sqlite3.connect('banco.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contas_curso WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    
    if usuario:
        while True:
            nova_senha = input("Digite sua nova senha: ").strip()
            if check_senha(nova_senha) == True:
                break
            else:
                print("Senha inválida! A senha deve conter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
        while True:
            confirmar_senha = input("Confirme sua nova senha: ").strip()
            if nova_senha == confirmar_senha:
                break
            else:
                print("As senhas não coincidem. Tente novamente.")
        if nova_senha == confirmar_senha:
            cursor.execute("UPDATE contas_curso SET senha = ? WHERE email = ?", (nova_senha, email))
            connection.commit()
            print("Senha atualizada com sucesso!")
        else:
            print("As senhas não coincidem. Tente novamente.")
    else:
        print("Email não encontrado. Verifique o email digitado.")
    
    connection.close()