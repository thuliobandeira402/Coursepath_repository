from deep_translator import GoogleTranslator
from time import sleep
from utils import *

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
            print(f"\033[1;32mIdioma alterado para {language}.​​✅​\033[0m")
            sleep(2)
            return
        else:
            print("\033[1;31mIdioma não suportado.​❌​ Mantendo o idioma atual.​\033[0m")
            sleep(2)