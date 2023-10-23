# Criar sistema de registro de usuarios
# - Pegar o nome de usuario, 
# - se o nome não tiver no minimo 8 caracteres o sistema vai negar a criação do usuario 
# - se a criação do usuario for negada o sistema vai pedir para o cliente inserir um novo nome de usuario
# - quando o nome de usuario for aceito o sistema vai pedir para o usuario colocar uma senha
# - a senha deve ter no minimo 10 caracteres
# - se a senha não for aceita o usuario deve inserir uma nova senha até que esta seja aceita
# - uando a senha e o usuario forem aceitos o loop termina e o programa acaba

while True:

    nome = input("digite o seu nome:")

    if len(nome) <= 7:
        print("permissao negada, insira um novo nome")
        continue
   
    print("Nome aceito pelo sistema, escolha sua senha")
    break

while True:

    senha = input("digite sua senha:")

    if len(senha) <= 9:
        print("A senha deve conter no minimo 10 caracteres")
        continue

    print("Senha aceita")
    break

#FEITO
#FEITO
#FEITO