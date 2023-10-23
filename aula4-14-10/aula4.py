F = "-=" * 30


def register_user(user):
    user_size = len(user)

    if user_size < 8:
        return f"Err: O tamanho do seu nickname deve ser maior que 8, faltam {8 - user_size}"
    elif user_size > 15:
        return f"Err: O tamanho do seu nickname deve ser menor que 15, retire {user_size - 15}"
    else:
        return "Usuario criada com sucesso!"


def register_password(password):
    psw_size = len(password)

    if psw_size < 10:
        return f"Err: O tamanho de sua password deve ser maior que 10, faltam {10 - psw_size}"
    
    elif psw_size > 17:
        return f"Err: O tamanho de sua password deve ser menor que 17, retire {psw_size - 17}"
    
    else:
        return "Senha criada com sucesso!"
        

while True:
    usr = input("Coloque seu usuario -> ")

    response = register_user(usr)
    print(F)
    print(response)

    if response == "Usuario criada com sucesso!":
        break
    else:
        continue


while True:
    print(F)
    psw = input("Coloque sua senha -> ")

    response = register_password(psw)
    print(F)
    print(response)

    if response == "Senha criada com sucesso!":
        break
    else:
        continue


print(F)
print(f"Conta com usuario {usr} e senha {len(psw) * '*'}, criada com sucesso!")