#8
import random

velocidade = (input("Qual era a velocidade no veículo no momento? "))

multa = 0

if velocidade:

    velocidade = float(velocidade)

    if velocidade < 30: 

        print("A velocidade do veículo está muito baixa, indique ao motorista que troque de mão. ")

    if velocidade > 90:

        valorMulta = velocidade - 90

        print(f"Devido a velocidade acima do permitido, o motorista deverá receber a multa num valor de {valorMulta * 7} reais. ")
        
else:   

    print("A velocidade não foi fornecida. ")

    numeroAleatorio = random.randint(1, 120)

    valorMultaAleatorio = numeroAleatorio * 7

    print(f"O valor da multa nessa situação será de {valorMultaAleatorio} reais. ")