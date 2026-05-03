# Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.

menor = None
positivos = 0
negativos = 0

while True:
    try:
        valor = float(input("Digite um valor real: "))

        if valor == 0:
            break
        
        if valor > 0:
            positivos += 1
        else:
            negativos += 1
        
        if menor is None or valor < menor:
            menor = valor 
    
    except ValueError:
        print("Entrada inválida. Digite um número.")

print(f"\nQuantidade de positivos : {positivos}")
print(f"Quatidade de negativos: {negativos}")

if menor is not None:
    print(f"O menor valor é: {menor}")
else:
    print("Nenhum valor foi inserido")

#grupo de pessoas

soma_homens = 0
qt_homens = 0

soma_mulheres = 0
qt_mulheres = 0 

while True:
    sexo = input("Digite seu sexo (M/F) ou Q para sair: ").upper()

    if sexo == 'Q':
        print("Obrigado!")
        break

    if sexo != 'M' and sexo != 'F':
        print("Digite um sexo válido!")
        continue

    try:
        altura = float(input("Digite sua altura: "))
    except:
        print("Altura inválida!")
        continue

    if sexo == 'M':
        soma_homens += altura
        qt_homens += 1
    else:
        soma_mulheres += altura
        qt_mulheres += 1

if qt_homens > 0:
    media_homens = soma_homens / qt_homens
    print(f"Média de altura dos homens: {media_homens:.2f}")
else:
    print("Nenhum homem foi encontrado")

if qt_mulheres > 0:
    media_mulheres = soma_mulheres / qt_mulheres
    print(f"Média de altura das mulheres: {media_mulheres:.2f}")
else:
    print("Nenhuma mulher foi encontrada")

# LER uma quantidade indeterminada de alunos com as infos

soma_geral = 0
qt_alunos = 0

maior = None
menor = None

soma_m = 0
qt_m = 0

soma_f = 0
qt_f = 0

while True:
    sexo = input("Digite seu o sexo (M ou F): ").lower()
    if sexo == 'q':
        print("Obrigado")
        break

    if sexo != 'm' and sexo != 'f':
        print("Digite m ou f")
        continue

    rgm = input("Qual seu rgm: ")
    if len(rgm) != 6 or not rgm.isdigit():
        print("Digite novamente!")
        continue

    nome = input("Nome da aluna(o): ")
    if not nome.replace(" ", "").isalpha():
        print("Digite seu nome!")
        continue

    try:
        nota1 = float(input("Digite sua nota1: "))
        nota2 = float(input("Digite sua nota2: "))
        nota3 = float(input("Digite sua nota3: "))
    except ValueError:
        print("INVALID!")
        continue

    media = (nota1 + nota2 + nota3) / 3

    soma_geral += media
    qt_alunos += 1

    if maior is None or media > maior:
        maior = media

    if menor is None or media < menor:
        menor = media

    if sexo == 'm':
        soma_m += media
        qt_m += 1
    else:
        soma_f += media
        qt_f += 1

if qt_alunos > 0:
    print(f"\nMédia da sala: {soma_geral / qt_alunos:.2f}")
    print(f"Maior média: {maior:.2f}")
    print(f"Menor média: {menor:.2f}")
else:
    print("Nenhum aluno cadastrado")

if qt_m > 0:
    print(f"Média masculina: {soma_m / qt_m:.2f}")
else:
    print("Nenhum homem cadastrado")

if qt_f > 0:
    print(f"Média feminina: {soma_f / qt_f:.2f}")
else:
    print("Nenhuma mulher cadastrada")

#ler produtos 
produtos = []

while True:
    entrada = input("Digite o código (ou 'sair'): ")
    
    if entrada.lower() == "sair":
        break

    try:
        codigo = int(entrada)
    except ValueError:
        print("Digite apenas números")
        continue
    descrição = input("Descrição: ")
    try:
        quantidade = float(input("Quantiadade de produtos que você vai levar: "))
        valor = float(input("Valor: "))
    except ValueError:
        print("Quantidade ou valor inválidado")
        continue

    produto = {
        "codigo": codigo,
        "descrição": descrição,
        "quantidade": quantidade,
        "valor": valor
    }

    produtos.append(produto)

total_venda = 0

for p in produtos:
    subtotal = p["quantidade"] * p["valor"]
    total_venda += subtotal

    print(f"Codigo: {p['codigo']}")
    print(f"descrição: {p['descrição']}")
    print(f"quantidade: {p['quantidade']}")
    print(f"valor unitario: {p['valor']:.2f}")
    print(f"subtotal: R$ {subtotal:.2f}")
    print("-" * 30)
    
print(f"\nTOTAL DA VENDA: R$ {total_venda:.2f}")





