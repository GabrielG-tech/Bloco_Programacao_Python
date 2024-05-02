# Analisador de Frequência de Letras
# Escreva um programa que analise a frequência de cada letra em um texto e retorne um histograma dessa frequência.

def contar_letras(texto):
    """
    Conta a frequência de cada letra em um texto.

    Argumentos:
    texto (str): O texto a ser analisado.

    Retorna:
    dict: Um dicionário contendo a contagem de cada letra presente no texto.
    """
    frequencia_letras = {}

    texto = texto.replace(" ", "").lower()

    for letra in texto:
        if letra.isalpha():
            if letra in frequencia_letras:
                frequencia_letras[letra] += 1
            else:
                frequencia_letras[letra] = 1

    return frequencia_letras

def histograma_frequencia(frequencia_letras):
    """
    Exibe um histograma da frequência de cada letra.

    Argumentos:
    frequencia_letras (dict): Um dicionário contendo a contagem de cada letra.

    Retorna:
    None
    """
    print("Histograma de Frequência de Letras:")
    for letra, frequencia in sorted(frequencia_letras.items()):
        print(f"{letra}: {'\033[1;41m● \033[m' * frequencia}")

texto = input("Digite o texto: ")
frequencia_letras = contar_letras(texto)
histograma_frequencia(frequencia_letras)
