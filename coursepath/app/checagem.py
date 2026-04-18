import re

def check_nome(nome):
    regra_nome = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*$')
    vn = re.fullmatch(regra_nome, nome)
    if vn:
        return True
    else:
        return False    




def check_email(email):
    # email precisa seguir a formatação NOME.SOBRENOME@UFRPE.BR
    regra_email = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@[uU][fF][rR][pP][eE]\.[bB][rR]$')
    ve = re.fullmatch(regra_email, email)
    if ve:
        return True
    else:
        return False

def check_senha(senha):
    # Senha precisa ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere 
    # especial
    if len(senha) < 8:
        return False
    elif not re.search(r'[A-Z]', senha):
        return False
    elif not re.search(r'[a-z]', senha):    
        return False
    elif not re.search(r'[0-9]', senha):
        return False
    elif not re.search(r'[!@#$%^&*(),.?"{}|<>]', senha):
        return False
    else:
        return True