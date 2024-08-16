nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Nome inválido. Por favor, digite um nome com mais de 3 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 100:
    print("Idade inválida. Por favor, digite uma idade entre 0 e 100.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Salário inválido. Por favor, digite um salário maior que zero.")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (f ou m): ")
while sexo not in ['f', 'm']:
    print("Sexo inválido. Por favor, digite f ou m.")
    sexo = input("Digite seu sexo (f ou m): ")

estado_civil = input("Digite seu estado civil (s, c, v, d): ")
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido. Por favor, digite s, c, v ou d.")
    estado_civil = input("Digite seu estado civil (s, c, v, d): ")

print("Informações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)