from deep_translator import GoogleTranslator
from time import sleep
from utils import *

# english: en

language = 'en'
idiomas_disponiveis = GoogleTranslator(source='auto', target='en').get_supported_languages(as_dict=True)

def translating_text(text):
    global language
    translator = GoogleTranslator(source='auto', target=language)
    translated = translator.translate(text)
    return translated


def change_language():
    global language
    while True:
        nova_lingua = input("Digite o idioma desejado (ex: 'en' para inglês, 'pt' para português) (Pode digitar o nome do idioma também): ").strip().lower()
        if nova_lingua in idiomas_disponiveis.keys() or nova_lingua in idiomas_disponiveis.values():
            language = nova_lingua
            print(f"Idioma alterado para {language}.")
            sleep(2)
            limpar_tela()
            return
        else:
            print("Idioma não suportado. Mantendo o idioma atual.")
            sleep(2)