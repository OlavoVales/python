# Estrutura de Controle de Fluxo:

# Estruturas Condicionais - If, Else, Elif()
# Estrutura de Repetição - While(Auxiliadores: Continue e Break)

#Desafios dessa aula: Operações Matématicas Básicas, Criação de conta, 1o RPG(Para Casa)1o Cavaleiro do Apocalipse)

# Operadores de comparação: 

## == e != funcionam pra qualquer tipo de dado primitivo(str,int,float,bool)

nome = "olavo"

# == significa: "é igual?"
nome == "joao" #False

# != significa: "é diferente?"
nome != "joao" #True

## >,<,<=,>= (funcionam com os tipos numericos(int e float))

idade = 19

# > :  "maior que?"
idade > 18 #True

# < : "menor que?"
idade < 18 #False

# >= : "maior ou igual que?"
idade >= 20 #False

# <= : "menor ou igual que?"
idade <= 19 #True



# Operadores lógicos: 

not True # = False




# Operadores de Associação

texto = "artigo"

"r" in texto #True



# Operadores de Identidade:

'''
X = 1001
Y = 1001

X == Y #True

X is Y #False

Id(X) #4417772080

Id(Y) #4417766416

You get False because you have two different instances of 1001 stored in your computer's memory

'''


#if, elif, else: Estruturas condicionais

cpfs_de_maior = "162.072.586-06182.392.716-50432.312.593.231-22999.888.777-16"

cpf_do_cliente = input("Me de seu cpf formatado em ###.###.###-## --> ")

if cpf_do_cliente in cpfs_de_maior:
    print("Entra ai fernando gracinha!")
else:
    print("Entrada proibida!")




idade = int(input("Qual a sua idade? -> "))

if idade == 18:
    print("Vou fazer uma verificação!")

elif idade < 18:
    print("Não pode entrar!")

else:
    print("Pode entrar direto barbudão!")




# While (loops)

while True:
    idade = int(input("coloque a idade -> "))

    if idade < 18:
        print(f"O numero que você colocou foi {idade} para chegar em 18 falta {18-idade}, adicione mais numeros!")
        continue # volta pro começo do loop(nesse caso por estar dentro dum if, volta pro começo caso a condição for cumprida)

    print("Sou maior de 18")
    break # Muda o estado pra false(mesmo que não esteja escrito true(estado padrão)) e acaba o loop

print("Programa acabou!")