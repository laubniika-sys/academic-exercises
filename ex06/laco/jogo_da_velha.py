def mostrar_tabuleiro(tab):
    print("\n")
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    print("\n")


def verificar_vitoria(tab, jogador):
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for combo in combinacoes:
        if tab[combo[0]] == tab[combo[1]] == tab[combo[2]] == jogador:
            return True
    return False


def jogo():
    tabuleiro = [" "] * 9
    jogador_atual = "X"
    jogadas = 0

    while jogadas < 9:
        mostrar_tabuleiro(tabuleiro)

        try:
            pos = int(input(f"Jogador {jogador_atual}, escolha (1-9): ")) - 1
        except ValueError:
            print("Entrada inválida!")
            continue

        if pos < 0 or pos > 8:
            print("Escolha entre 1 e 9!")
            continue

        if tabuleiro[pos] != " ":
            print("Essa posição já está ocupada!")
            continue

        tabuleiro[pos] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f" Jogador {jogador_atual} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    mostrar_tabuleiro(tabuleiro)
    print("Deu velha!")


if __name__ == "__main__":
    jogo()