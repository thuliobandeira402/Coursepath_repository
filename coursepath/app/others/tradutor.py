from deep_translator import GoogleTranslator
from time import sleep
from others.utils import *

language = 'en'
idiomas_disponiveis = GoogleTranslator(source='auto', target='en').get_supported_languages(as_dict=True)

def translating_text(text):
    global language
    translator = GoogleTranslator(source='auto', target=language)
    translated = translator.translate(text)
    return translated

def imprimir_cabecalho_idiomas():
    print("\033[1;36m=\033[0m"*50)
    print("\033[1;36m|            Configurações de Idioma             |\033[0m")
    print("\033[1;36m=\033[0m"*50)

def menu_idiomas():
    while True:
        imprimir_cabecalho_idiomas()
        change_language()
        limpar_tela()
        break



def change_language():
    global language
    while True:
        nova_lingua = input("""Digite o idioma desejado:
\033[1;34m[en]\033[0m para inglês   \033[1;34m[pt]\033[0m para português \033[1;34m[es]\033[0m para espanhol    
\033[1;34m[fr]\033[0m para francês  \033[1;34m[de]\033[0m para alemão    \033[1;34m[it]\033[0m para italiano
\033[1;34m[ru]\033[0m para russo    \033[1;34m[ja]\033[0m para japonês   \033[1;34m[zh]\033[0m para chinês

Opção:
    """).strip().lower()
        if nova_lingua in idiomas_disponiveis.keys() or nova_lingua in idiomas_disponiveis.values():
            language = nova_lingua
            print(f"\033[1;32mIdioma alterado para {language}.​​✅​\033[0m")
            sleep(2)
            return
        else:
            print("\033[1;31mIdioma não suportado.​❌​ Mantendo o idioma atual.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho_idiomas()


def traduzir_e_printar():
    change_language()
    print("Carregando o texto traduzido...🔄​")
    sleep(2)
    limpar_tela()
   