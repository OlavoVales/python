
numero1str = input("Digite o 1o número: ")

numero2str = input("Digite o 2o número: ")

numero1 = int(numero1str)

numero2 = int(numero2str)

print(numero1 + numero2)

print(numero1 - numero2)

print(numero1 * numero2)

print(numero1 / numero2)





def capturar_dados():
    
    num1 = int(input("Digite o 1o número: "))

    num2= int(input("Digite o 2o número: "))

    return num1, num2

def soma(x,y): #valor de substituição (placeholder), simplismente pra segurar o dado fornecido
    
    return x + y

def subtracao(x,y):
    
    return x - y

def multiplicacao(x,y):
    
    return x * y

def divisao(x,y):
    
    return x / y


num1, num2 = capturar_dados()
soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1,num2)
divisao(num1,num2)




def capturar_dados():
    
    num1 = int(input("Digite o 1o número: "))

    num2= int(input("Digite o 2o número: "))

    return num1, num2

def soma(x,y): #valor de substituição (placeholder), simplismente pra segurar o dado fornecido
    
    print(f'o valor de x é {x} e o valor de y é {y} e a soma dos dois é {x + y}') #int

def subtracao(x,y):
    
    print(f'o valor de x é {x} e o valor de y é {y} e a subtracao dos dois é {x - y}') #int

def multiplicacao(x,y):
    
    print(f'o valor de x é {x} e o valor de y é {y} e a multiplicacao dos dois é {x * y}') #int

def divisao(x,y):
    
    print(f'o valor de x é {x} e o valor de y é {y} e a divisao dos dois é {x / y}') #float


num1, num2 = capturar_dados()
soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1,num2)
divisao(num1,num2)

#exemplo função básica:

def media(a, b):
    return (a+b)/2

x = media(1, 3)

print(x)


# Parameters and arguments

def add(a, b):          #the parameter is what is declared in the function, 
#                       #while an argument is what is passed through when calling the function.
    return (a + b)          
#                       #a and b are the PARAMETERS, 5 and 4 are the ARGUMENTS
add(5, 4)





# pudim = 1;pudim2 = 2 <-certo, pudim 1 pudim 2 <- errado(Statements must be separated by newlines or semicolons)




;texto1 = houhouhou  *tem um ; escondido no inicio de cada linha, pro interpretador saber que ele terminou de ler aquela linha*
;texto2 = hihihi
