import os
from deep_translator import GoogleTranslator
def translating_text(text):
    translator = GoogleTranslator(source='auto', target='en')
    translated = translator.translate(text)
    return translated

def variable_options(in_portuguese):
    if in_portuguese:
        print("""1. Prosseguir para o menu de estudos extra sobre o curso
2. Voltar para o menu de cursos
3. Traduzir para o idioma anterior""")
    else:
        print("""1. Prosseguir para o menu de estudos extra sobre o curso
2. Voltar para o menu de cursos
3. Traduzir para Português""")
  

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
