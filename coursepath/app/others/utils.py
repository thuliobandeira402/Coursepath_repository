import os
from deep_translator import GoogleTranslator


def variable_options(in_portuguese):
    """"função que cria 2 variaveis para o menu de um curso, varia de acordo com
    o idioma do texto"""
    if in_portuguese:
        print("""\033[1;34m1.\033[0m Prosseguir para o menu de estudos extra sobre o curso
\033[1;34m2.\033[0m Voltar para o menu de cursos
\033[1;34m3.\033[0m Traduzir para o idioma anterior""")
    else:
        print("""\033[1;34m[1].\033[0m Prosseguir para o menu de estudos extra sobre o curso
\033[1;34m[2].\033[0m Voltar para o menu de cursos
\033[1;34m[3].\033[0m Traduzir para Português""")
  

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def variable_options_cadeiras(in_portuguese):
    """Menu que varia as opções para o menu de cadeiras, varia de acordo com
    o idioma do texto"""
    if in_portuguese:
        print("""\033[1;34m1.\033[0m Artigo 01
\033[1;34m2.\033[0m Artigo 02
\033[1;34m3.\033[0m Traduzir para o idioma anterior
\033[1;34m4.\033[0m Sair""")
        
    else:
        print("""\033[1;34m[1].\033[0m Artigo 01
\033[1;34m[2].\033[0m Artigo 02
\033[1;34m[3].\033[0m Traduzir para Português
\033[1;34m[4].\033[0m Sair""")
        
def variable_options_articles(in_portuguese):
    """Menu que varia as opções para o menu de artigo, varia de acordo com
    o idioma do texto"""
    if in_portuguese:
        print("""\033[1;34m[1].\033[0m Traduzir para o idioma anterior
\033[1;34m[2].\033[0m Sair""")
        
    else:
        print("""\033[1;34m[1].\033[0m Traduzir para Português
\033[1;34m[2].\033[0m Sair""")
        
def variable_options_addarticle(in_portuguese):
    """Menu que varia as opções para o menu de adicionar artigo, varia de acordo com
    o idioma do texto"""
    if in_portuguese:
        print("""\033[1;34m[1]\033[0m. Alterar idioma
\033[1;34m[2]\033[0m. Traduzir para o idioma anterior
\033[1;34m[3]\033[0m. Sair""")    
    else:
        print("""\033[1;34m[1]\033[0m. Alterar idioma
\033[1;34m[2]\033[0m. Traduzir para português
\033[1;34m[3]\033[0m. Sair""")