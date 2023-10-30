'''
1)Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. #CERTO
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2)O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor 
e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, 
escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. #CERTO
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3)Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores. #CERTO
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
4)Escreva um programa que leia um valor em reais e passe para dólares #CERTO
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
5)Escreva um programa que leia os catetos oposto e adjacente de um triângulo e calcule a hipotenusa
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
6)Crie um programa que peça ao usuário um número, e retorne todos os múltiplos do número escolhido pelo usuário de 1 a 10
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
7)Use a estrutura de loop para que o programa retorne todos os múltiplos de 6 de 0 a 500.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
8)Simule um radar de rodovia 
Onde a velocidade máxima permitida na rodovia é 90 Km/h e a mínima 30 Km/h
-O programa deve capturar a velocidade do usuário por terminal, caso a resposta esteja em branco o programa deve indicar que a velocidade não foi fornecida
-Caso o usuário esteja abaixo da velocidade o programa deve retornar que o carro está muito lento e que o usuário deve mudar de mão
-Caso o usuário esteja acima da velocidade o programa deve computar uma multa para o usuário, sendo o valor dessa multa o excesso de velocidade * 7
-Caso a velocidade não seja fornecida pelo usuário o programa deve sortear um numero entre 1 e 120 e aplicar a mecânica acima com o numero sorteado
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''


'''

#1

idade = int(input("qual a sua idade em anos? "))
meses = int(input("quantos meses de idade? "))
dias = int(input("quantos dias de idade?" ))

diasIdade = ((idade * 365) + (meses * 30) + dias)

print(f"A sua idade expressa em dias é: {diasIdade}")

#CERTO

'''




'''

#2

custoFabrica = int(input("informe o custo de fabrica do carro: "))

percentualDistribuidor = (custoFabrica * 1.28)

impostos = (custoFabrica * 1.45)

custoFinalConsumidor = (percentualDistribuidor + impostos)

print(f"o custo final  para o consumidor é de {custoFinalConsumidor} reais")

#CERTO

'''




'''

#3

quantidadeEleitores = int(input("qual a quantidade de eleitores? "))

votosBrancos = int(input("qual a quantidade de votos brancos? "))

votosNulos = int(input("qual a quantidade de votos nulos? "))

votosValidos = int(input("qual a quantidade de votos válidos? "))

votos = (votosBrancos + votosNulos + votosValidos)

if quantidadeEleitores != votos:
    print("a quantidade votos informada está incorreta, favor verificar novamente")

porcentagemvVotosBrancos = ((votosBrancos / quantidadeEleitores) * 100)

porcentagemvVotosNulos = ((votosNulos / quantidadeEleitores) * 100)

porcentagemvVotosValidos = ((votosValidos / quantidadeEleitores) * 100)

print(f"em relação a quantidade total de eleitores,os votos brancos representam {porcentagemvVotosBrancos}% do total, os votos nulos {porcentagemvVotosNulos}% e os votos válidos {porcentagemvVotosValidos}%")

#CERTO

'''




'''

#4

real= int(input("escreva a quantidade de reais que você transformar em dolár: "))

realPraDolar = ((real / 4.98))

dolar = print(f"sua quantidade de doláres é: {realPraDolar}")

#CERTO

'''




#5

