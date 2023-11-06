# CÓDIGO TODO JUNTO, SEPARAR DEPOIS
# CÓDIGO TODO JUNTO, SEPARAR DEPOIS
# CÓDIGO TODO JUNTO, SEPARAR DEPOIS
# CÓDIGO TODO JUNTO, SEPARAR DEPOIS
# CÓDIGO TODO JUNTO, SEPARAR DEPOIS


'''
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
NAO CHAMAR UMA FUNÇÃO DENTRO DE OUTRA FUNÇÃO
'''

import random

#PARTE 1

def choice_caracter():
    
    while True:

        classePersonagem = input("Welcome to the Console RPG. Choose your class: Warrior (W) or Mage (M): ")

        if classePersonagem == "W":
            return "WARRIOR"
        elif classePersonagem == "M":
            return "MAGE"
        else:
            print("The informed class is incorrect, please select a valid one. ")
            continue

def power(character):
    if character == "WARRIOR":
        random.randint(5,10)
    elif character == "MAGE":
        random.randint(7,15)

# PARTE 2

