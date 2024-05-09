# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print("|".join(linha))
        if i != 2: 
            print("-" * 11)

# Função para verificar se alguém ganhou
def verificar_ganhador(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "   ":
            return linha[0]

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "   ":
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "   ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "   ":
        return tabuleiro[0][2]

    # Se não houver ganhador
    return None

# Criar tabuleiro vazio
tabuleiro = [["   " for _ in range(3)] for _ in range(3)]

# Loop do jogo
jogador_atual = "X"
while True:
    # Imprimir o tabuleiro atual
    print("Tabuleiro atual:")
    imprimir_tabuleiro(tabuleiro)

    # Obter a jogada do jogador
    linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1, 2 ou 3): ")) -1
    coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1, 2 ou 3): ")) -1

    # Verificar se a posição está vazia
    if tabuleiro[linha][coluna] == "   ":
        # Realizar a jogada
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se há um ganhador
        ganhador = verificar_ganhador(tabuleiro)
        if ganhador:
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {ganhador} venceu!")
            break
        elif all(all(c != "   " for c in linha) for linha in tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Deu velha!")
            break

        # Trocar para o próximo jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Posição já ocupada. Escolha outra.")
