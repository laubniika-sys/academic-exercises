#calcular a area do voluem

h = float(input("Digite o valor da altura: "))
bmenor = float(input("Digite o valor da Bmenor: "))
bmaior = float(input("Digite o valor da Bmaior: "))

volume = (h/3) *(bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2)**0.5)

print(f"O volume é igual a {volume:.2f}")

#solitar o vlaor em horas para o usuário

valor = float(input("Digite para converter em horas: "))
horas = 60

valor_convertido_min = valor * horas
print(f"{valor} em horas, é {valor_convertido_min} minutos")

#idade do usuario
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

total_dias = (anos * 365) + (meses * 30) + dias
print(f"Sua idade em dias é: {total_dias} dias")

#calcular valor da prestação em atraso

valorPrestacao = float(input("Digite o valor original da prestação: R$ "))
multa = float(input("Digite a porcentagem de multa: "))
qtdeDias = int(input("Digite a quantidade de dias em atraso: "))

prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qtdeDias)

print("-" * 30)
print(f"Valor original: R$ {valorPrestacao:.2f}")
print(f"Dias em atraso: {qtdeDias}")
print(f"Multa: {multa}%")
print(f"Valor atualizado: R$ {prestacao:.2f}")
print("-" * 30)

#radianos

import math

graus = float(input("Digite o valor do ângulo em graus: "))

radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"Ângulo: {graus}°")
print(f"Radianos: {radianos:.4f}")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")
