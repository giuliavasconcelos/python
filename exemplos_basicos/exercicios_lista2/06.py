comida = int(input("Indique a opção desejada: "))

# Seleção de opções
match comida:
    case 1:
        print("Pizza. ")
    case 2:
        print("Hamburguer. ")
    case 3:
        print("Salada. ")
    case _:
        print("Opção inválida!")