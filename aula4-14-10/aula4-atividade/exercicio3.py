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