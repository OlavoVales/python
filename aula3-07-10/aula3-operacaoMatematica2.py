# informar um numero
# multiplicar este numero de 1 a 100
# caso esse numero for par, aparecer no console
# quando a multiplicação chegar a 100, parar o processo

numero = int(input("informe um numero qualquer de 1 a 10: "))

x = 1

while True:
    numero2 = numero * x

    if numero2 % 2 == 0:
     print(f"esses são so numero pares de {numero} vezes {x} : {numero2}") #tem que fazer

    x = x + 1

    if x == 100:
        break