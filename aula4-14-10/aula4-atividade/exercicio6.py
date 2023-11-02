#6

numeroBase = float(input("informe qualquer número desejado: "))

x = 0

while True:

    x += 1  # x += x + 1, += pega o valor depois do sinal e adiciona a variavel, nesse caso pegando o proprio valor da variavel e adicionando ela mesma e mais 1, x(0) +=  x(0) + 1 == 1, x(1) += x(1) + 1 == 3,
 #                                                                                                                                                                                        x(3) += x(3) + 1 == 7,
 #                                                                                                                                       pega o proprio valor, soma com oque está depois do += e dá o resultado.
    numero2 = numeroBase * x

    if x > 10:
        break

    print(f"o numero escolhido: {numeroBase} vezes {x}, é igual a: {numero2}")

#FEITO