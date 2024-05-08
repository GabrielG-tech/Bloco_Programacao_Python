# Nivel 1 - Ex 1
# Crie uma função que recebe uma matriz (lista de listas) e exiba a transposta desta matriz, no formato devido de linhas e colunas.

def transposta(matriz):
    if not matriz:
        return []

    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Inicializa a matriz transposta só com zeros
    matriz_transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    # Troca os valores zerados pela matriz transposta
    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz_transposta[j][i] = matriz[i][j]

    return matriz_transposta


matriz = [
    [1, 5],
    [7, 3],
    [8, 2]
]
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

transposta_resultado = transposta(matriz)

print("Matriz Original:")
for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")
for linha in transposta_resultado:
    print(linha)
