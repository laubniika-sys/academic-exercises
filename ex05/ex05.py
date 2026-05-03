# valor da venda

produto = input("Nome do produto: ")
price = float(input("Valor de compra: R$ "))

if price < 10:
    profit = price * 1.70
elif 10 <= price < 30:
    profit = price * 1.50
elif 30 <= price < 50:
    profit = price * 1.40
else:  # price >= 50
    profit = price * 1.30

print(f"Produto: {produto}")
print(f"Valor de venda: R$ {profit:.2f}")
#calculator

print("Calculadora de dois valores!")
num1 = float(input("First number: "))
operator = input("Select an operator (+ - * /) : ")
num2 = float(input("Second number: "))

while True:
    if operator == '+':
        result = num1 + num2
        print(f"The result is {result}")
        break
    elif operator == '-':
        result = num1 - num2
        print(f"The result is {result}")
        break
    elif operator == '*':
        result = num1 * num2
        print(f"The result is {result}")
        break
    elif operator == '/':
        result = num1 / num2
        print(f"The result is {result}")
        break
    else:
        print("VALUE ERROR!!")
        break

#leitrua de numeros inteiros 
num = []
for i in range(4):
    nume = int(input(f"Digite o {i + 1} numero: "))
    num.append(nume)

print("Maior: ", max(num))
print("Menor: ", min(num))

#ler 5 numeros

numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("O maior número é:", max(numeros))




   
