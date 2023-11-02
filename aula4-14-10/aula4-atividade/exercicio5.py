#5

import math

valorBaseCatetoOposto = float(input("informe a medida do cateto oposto: "))
valorBaseCatetoAdjacente = float(input("informe a medida do cateto adjacente: "))

hipotenusa = math.sqrt(valorBaseCatetoOposto * valorBaseCatetoOposto + valorBaseCatetoAdjacente * valorBaseCatetoAdjacente)

print(f"o valor da hipotenusa é: {hipotenusa}")

#CERTO