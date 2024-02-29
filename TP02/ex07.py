# Função com Parâmetros Padrões
# Problema: Implemente uma função que desenhe uma linha padrão na tela sem que sejam passados argumentos para a função, porém aceitando como parâmetros definidos por posição um caractere para construir a linha e o comprimento da linha.

def desenhar_linha(caractere='-', comprimento=25):
    """
    Desenha uma linha na tela usando um caractere especificado e um comprimento.

    Parâmetros:
    - caractere (str): O caractere usado para desenhar a linha. O padrão é '-'.
    - comprimento (int): O comprimento da linha a ser desenhada. O padrão é 10.
    """
    # Desenha a linha na tela
    print(caractere * comprimento)

# Chamada da função sem argumentos (usando os padrões)
desenhar_linha()

# Chamada da função com argumentos específicos
desenhar_linha('*', 20)
