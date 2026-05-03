# area do retangulo

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# salário acrescido de 5%
salario = float(input("Digite o salário: "))
salario_acrescimo = salario * 1.05

print("O salário com acréscimo é", salario_acrescimo)

# distancia entre duas cidades

distancia1 = float(input("Distancia em km: "))
tempo = float(input("Digite o tempo de viagem (em horas): "))

if tempo > 0:
    Vm = distancia1 / tempo
    print(f"A velocidade média do carro é de {Vm} km/h")
else:
    print("Error!")

# escreva um programa que calcule as esquações de segundo grau
import math 

valor1 = int(input("valor1: "))
valor2 = int(input("valor2: "))
valor3 = int(input("valor3: "))

delta = valor2 * valor2 - 4 * valor1 * valor3

if delta < 0:
    print("Digite um valor válido!")
else: 
    x1 = (-valor2 + math.sqrt(delta)) / (2 * valor1)
    x2 = (-valor2 - math.sqrt(delta)) / (2 * valor1)

    print(f"Delta: {delta}")
    print(f"x1: {x1}")
    print(f"x2:{x2}")

#Conversor
taxa_cambio = float(input("Digite a cotação do dólar: "))
dolar = float(input("Digite o valor em dólar: "))
real = dolar * taxa_cambio
print(f"US${dolar:.2f} equivale a R${real:.2f}")
# restaurante

# Lê o valor do consumo
gasto = float(input("Digite o valor gasto no restaurante: R$ "))

gorjeta = gasto * 0.10

total = gasto + gorjeta

print(f"\n--- Resumo da Conta ---")
print(f"Valor do consumo: R$ {gasto:.2f}")
print(f"Gorjeta do garçom (10%): R$ {gorjeta:.2f}")
print(f"Valor total a ser pago: R$ {total:.2f}")

# celsuis e fahrenheit

celsius = float(input("Digite a temperatura em graus Celsius (°C): "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\n--- Conversão de Temperatura ---")
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F (Fahrenheit)")
print(f"{celsius}°C equivale a {kelvin:.2f}K (Kelvin)")

