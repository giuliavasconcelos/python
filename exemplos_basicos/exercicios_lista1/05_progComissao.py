# Valores
produto = float(input("\nInsira o valor do Produto: "))
percent = float(input("Insira a porcentagem da comissão: "))

# Calculo
result = (produto * (percent / 100))

# Resultado
print(f"A sua comissão é de R${result}\n")