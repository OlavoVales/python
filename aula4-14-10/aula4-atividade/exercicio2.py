#2

custoFabrica = int(input("informe o custo de fabrica do carro: "))

percentualDistribuidor = (custoFabrica * 1.28)

impostos = (custoFabrica * 1.45)

custoFinalConsumidor = (percentualDistribuidor + impostos)

print(f"o custo final  para o consumidor é de {custoFinalConsumidor} reais")

#CERTO