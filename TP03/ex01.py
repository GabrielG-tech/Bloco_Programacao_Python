# Contador de Vogais e Consoantes
# Escreva um script que conte o número de vogais e consoantes em uma frase fornecida pelo usuário.

def contar_vogais_consoantes(frase):
    """
    Esta função conta o número de vogais e consoantes em uma frase.

    Argumentos:
    frase (str): A frase fornecida pelo usuário.

    Retorna:
    tuple: Uma tupla contendo o número de vogais e o número de consoantes na frase.
    """

    lista_vogais = "aeiouâêîôûãõáéíóúàèìòù"
    lista_consoantes = "bcdfghjklmnpqrstvwxyz"

    vogais = 0
    consoantes = 0

    for char in frase:
        if char.isalpha():  # Verifica se o caractere é uma letra
            if char in lista_vogais:
                vogais += 1
            elif char in lista_consoantes:
                consoantes += 1

    return vogais, consoantes

frase = input("Escreva uma frase para contagem: ").lower()
num_vogais, num_consoantes = contar_vogais_consoantes(frase)
print("Número de Vogais:", num_vogais)
print("Número de Consoantes:", num_consoantes)