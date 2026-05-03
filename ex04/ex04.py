# if (0-9)
num = int(input("Escreva um número (0-9): "))

if 0 <= num <= 9:
    print("Valor correto")
else:
    print("Valor incorreto!")

# trabalho

horas_trabalho = float(input("Quantas horas você trabalhou hoje: "))
turno = input("Digite o seu turno (N para noturno e D para diurno): ")

if turno.upper()== 'N:
    valor_hora = 45.00
else:
    valor_hora = 37.5

salario = valor_hora * horas_trabalho

print(f"O valor da horas é de {valor_hora}")
print(f"O salário é de {salario}")

#supermarket

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    valor_desconto = valor_compra * 0.8
    print(f"O valor da compra foi de {valor_compra}")
    print(f"O valor da compra com o desconto é de {valor_desconto}")
else:
    print(f"O valor foi de {valor_compra}")

# contas de casa

agua = float(input("Quanto você gastou em água: R$"))
luz = float(input("Quanto você gastou em luz: R$"))
telefone = float(input("Quanto você gastou em telefone: R$"))
salario = float(input("Qual o valor do seu salário: R$"))

total_contas = agua + luz + telefone

if salario < total_contas:
    print("Salário insuficiente!")
else:
    resto = salario - total_contas
    print(f"O resto do seu salário após as contas foi de {resto}")