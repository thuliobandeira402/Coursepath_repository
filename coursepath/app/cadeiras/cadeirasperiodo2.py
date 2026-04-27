from others.utils import *
from others.tradutor import *
import textwrap
from time import sleep
from articles.artigos_periodo2 import *

INTRODUCTION_TEXT_FUNDAMENTOSMATEMATICOS01 = ("""Os fundamentos matemáticos para Sistemas de Informação (SI) formam a base teórica e prática para o desenvolvimento de software,
 algoritmos, segurança e análise de dados. Esta área combina a lógica rigorosa com estruturas discretas para modelar problemas computacionais.""")

INTRODUCTION_TEXT_PROJETOINTERDISCIPLINAR02 = ("""O projeto interdisciplinar em Sistemas de Informação visa integrar conhecimentos teóricos e práticos de diversas disciplinas 
para desenvolver soluções tecnológicas reais (softwares, aplicativos, análise de dados) a problemas organizacionais. Geralmente focado no desenvolvimento 
de sistemas, gestão de TI ou segurança, promove trabalho em equipe e metodologias ágeis.""")

INTRODUCTION_TEXT_FUNDAMENTOSDEPROBLEMASCOMPUTACIONAIS = ("""Os Fundamentos de Sistemas de Informação (SI) constituem a base teórica e prática para o entendimento de como dados são transformados
 em informações úteis para a tomada de decisão nas organizações. Eles interligam tecnologia, processos e pessoas para atingir objetivos organizacionais.""")

INTRODUCTION_TEXT_ELEMENTOSDESISTEMASCOMPUTACIONAIS = ("""Sistemas de informação utilizam elementos computacionais inter-relacionados para processar dados brutos em informações úteis. Os componentes
essenciais são hardware (equipamentos físicos), software (programas e instruções), pessoas (usuários e técnicos), dados/banco de dados e redes de comunicação, visando suporte à tomada de decisão e gestão
organizacional.""")

INTRODUCTION_TEXT_FUNDAMENTOSDESSISTEMASDEINFORMACAO =("""Um Sistema de Informação é um conjunto de componentes inter-relacionados que trabalham juntos para coletar, processar, armazenar e distribuir
informações, visando apoiar a tomada de decisão, a coordenação e o controle dentro de uma organização. Eles não apenas automatizam tarefas, mas integram dados para proporcionar uma visão holística dos negócios.""")


def fundamentos_matematicos02_menu():
    in_portuguese = False
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*100)
            print("\033[1;36m|                                    FUNDAMENTOS MATEMÁTICOS 02                                    |\033[0m")
            print("\033[1;36m=\033[0m"*100)
        imprimir_cabecalho()
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_FUNDAMENTOSMATEMATICOS01, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_FUNDAMENTOSMATEMATICOS01)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*100)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            print(formatted)
            print("\033[1;36m=\033[0m"*101)
            variable_options_cadeiras(in_portuguese)
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_01_algebra_linear()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_02_algebra_linear()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
        elif escolha == "4":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def projeto_interdisciplinar02_menu():
    in_portuguese = False
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*101)
            print("\033[1;36m|                                    PROJETO INTERDISCIPLINAR 02                                    |\033[0m")
            print("\033[1;36m=\033[0m"*101)
        imprimir_cabecalho()
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_PROJETOINTERDISCIPLINAR02, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_PROJETOINTERDISCIPLINAR02)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*101)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            print(formatted)
            print("\033[1;36m=\033[0m"*101)
            variable_options_cadeiras(in_portuguese)
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_01_metodologia()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_02_metodologia()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
        elif escolha == "4":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break

def fundamentos_de_problemas_computacionais_menu():
    in_portuguese = False
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*110)
            print("\033[1;36m|                                   FUNDAMENTOS DE PROBLEMAS COMPUTACIONAIS                                  |\033[0m")
            print("\033[1;36m=\033[0m"*110)
        imprimir_cabecalho()
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_FUNDAMENTOSDEPROBLEMASCOMPUTACIONAIS, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_FUNDAMENTOSDEPROBLEMASCOMPUTACIONAIS)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*110)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            print(formatted)
            print("\033[1;36m=\033[0m"*110)
            variable_options_cadeiras(in_portuguese)
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_01_fundamentos_computacionais()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_02_fundamentos_computacionais()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
        elif escolha == "4":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break

def elementos_de_sistemas_computacionais_menu():
    in_portuguese = False
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*110)
            print("\033[1;36m|                                   ELEMENTOS DE SISTEMAS COMPUTACIONAIS                                     |\033[0m")
            print("\033[1;36m=\033[0m"*110)
        imprimir_cabecalho()
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_ELEMENTOSDESISTEMASCOMPUTACIONAIS, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_ELEMENTOSDESISTEMASCOMPUTACIONAIS)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*110)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            print(formatted)
            print("\033[1;36m=\033[0m"*110)
            variable_options_cadeiras(in_portuguese)
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_01_elementos_sistemas()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_02_elementos_sistemas()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
        elif escolha == "4":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break


def fundamentos_de_sistemas_de_informacao_menu():
    in_portuguese = False
    while True:
        def imprimir_cabecalho():
            print("\033[1;36m=\033[0m"*110)
            print("\033[1;36m|                                   FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO                                    |\033[0m")
            print("\033[1;36m=\033[0m"*110)
        imprimir_cabecalho()
        if in_portuguese:
            formatted = textwrap.fill(INTRODUCTION_TEXT_FUNDAMENTOSDESSISTEMASDEINFORMACAO, width=80)
        else:
            translated = translating_text(INTRODUCTION_TEXT_FUNDAMENTOSDESSISTEMASDEINFORMACAO)
            formatted = textwrap.fill(translated, width=80)
        print(formatted)
        print("\033[1;36m=\033[0m"*110)
        variable_options_cadeiras(in_portuguese)
        escolha = input("Opção: ").strip()
        while escolha not in ["1", "2", "3", "4"]:
            print("\033[1;31mOpção inválida.❌​ Tente novamente.​\033[0m")
            sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            print(formatted)
            print("\033[1;36m=\033[0m"*110)
            variable_options_cadeiras(in_portuguese)
            escolha = input("Opção: ").strip()
        if escolha == "1":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_01_sistemas_informacao()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "2":
            print("\033[1;33mCARREGANDO...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            menu = artigos_02_sistemas_informacao()
            if menu == 'menu_principal':
                return 'menu_principal'
        elif escolha == "3" and in_portuguese:
            in_portuguese = False
            sleep(2)
            limpar_tela()
        elif escolha == "3":
            in_portuguese = True
            sleep(2)
            limpar_tela() 
        elif escolha == "4":
            print("\033[1;33mVoltando para o menu de cadeiras...🔄​\033[0m")
            sleep(2)
            limpar_tela()
            break