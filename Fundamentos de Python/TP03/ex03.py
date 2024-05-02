# Calculadora de Média com Suporte a Diferentes Separadores Decimais
# Crie um programa que solicite ao usuário uma sequência de números separados por espaço, aceitando tanto o ponto (.) quanto a vírgula (,) como separadores decimais. O programa deve calcular e exibir a média desses números.

def calcular_media(numeros):
    """
    Calcula a média dos números fornecidos.

    Argumentos:
    numeros (str): Uma sequência de números, podendo ser decimais e separados por espaços.

    Retorna:
    float: A média dos números.
    """
    soma = 0
    for n in numeros.split():
        soma += float(n.replace(",", "."))
    return soma / len(numeros)

numeros = input("Digite uma sequência de números (podendo ser decimais): ")
media = calcular_media(numeros)
print(f"A média dos números é: {media}")
