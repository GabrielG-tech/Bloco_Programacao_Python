def imprimir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print("|".join(linha))
        if i != 2: 
            print("-" * 5 + "+" + "-" * 5 + "+"+ "-" * 5)

def verificar_ganhador(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "   ":
            return linha[0]

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "   ":
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "   ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "   ":
        return tabuleiro[0][2]

    return False

def jogar(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == "   ":
        tabuleiro[linha][coluna] = " " + jogador + " "
        return True
    else:
        print("Essa posição já está ocupada. Tente novamente.")
        return False

def jogar_velha(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == "   ":
                return False
    return True

def tratar_input(mensagem):
    while True:
        try:
            posicao = int(input(mensagem)) - 1
            if posicao in [0, 1, 2]:
                return posicao
            else:
                print("Valor inserido está incorreto, tente novamente.")
        except ValueError:
            print("Valor inserido deve ser um número, tente novamente.")

def jogo_da_velha():
    # Inicialização do tabuleiro
    tabuleiro = [["   " for _ in range(3)] for _ in range(3)]
    imprimir_tabuleiro(tabuleiro)

    jogador_atual = 'X'

    while True:
        linha = tratar_input(f"Jogador {jogador_atual}: Escolha a linha (1, 2 ou 3): ", "linha")
        coluna = tratar_input(f"Jogador {jogador_atual}: Escolha a coluna (1, 2 ou 3): ", "coluna")

        if jogar(tabuleiro, linha, coluna, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            vencedor = verificar_ganhador(tabuleiro)
            if vencedor:
                print(f"Parabéns, jogador {vencedor.strip()}! Você ganhou!")
                break
            elif jogar_velha(tabuleiro):
                print("Deu velha!")
                break
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        repetir = input("Deseja jogar novamente? (sim/não): ").lower().strip()
    return repetir == "sim" or repetir == "s"

while True:
    if not jogo_da_velha():
        print("Obrigado por jogar! Até a próxima!")
        break
