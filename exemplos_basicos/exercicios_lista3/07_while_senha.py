i = 1
while i <= 3:
    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if user != "Gisele" and senha != "1234":
        print("Usuario ou senha invalidos")
        print(" ")

    else:
        print(" ")
        print(f"Bem vindo, {user}!")
        break

else:
    print(f"Você excedeu toas as: {i-1} tentativas.")