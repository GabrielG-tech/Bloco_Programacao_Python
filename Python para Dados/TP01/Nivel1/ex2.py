# Nivel 1 - Ex 2
# Crie uma matriz 3x3 (lista de listas) que representa um tabuleiro de jogo da velha, inicialmente vazio, onde cada célula vazia é representada por um espaço em branco " " e imprima este tabuleiro. Em seguida, o código deve permitir à dois usuários adicionar 'X' ou 'O' em posições específicas e checar se um dos dois ganhou naquela jogada, antes do próximo jogador inserir a coordenada da sua jogada e informar se o resultado foi a vitória de um dos dois ou se deu “velha”.

matriz = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

tabuleiro_vazio = criar_tabuleiro()
imprimir_tabuleiro(tabuleiro_vazio)
