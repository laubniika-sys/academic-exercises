while True:
    try:
        n = int(input("Digite a quantidade de termos: "))
        if n <= 0:
            print("Digite um número positivo!")
            continue
        
        t1 = 0
        t2 = 1

        if n >= 1:
            print(f"{t1} ", end="")
        if n >= 2:
            print(f"{t2} ", end="")


        cont = 3
        while cont <= n:
            t3 = t2 + t1
            print(f"{t3} ", end="")
            t1 = t2
            t2 = t3
            cont +=1
        break
    except ValueError:
        print("INVALID!")
