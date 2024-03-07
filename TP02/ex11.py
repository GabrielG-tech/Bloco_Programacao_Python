# Ordenador de Lista por Tamanho de Palavra
# Problema: Implemente um programa que organize uma lista de palavras em ordem crescente de tamanho.

lista = ["12345", "1234", "1234567", "12345", "12345678", "123456789", "123"]
lista_ordenada = sorted(lista, key=len)

def filtrar_por_tamanho(lista):
    """
    Filtra uma lista de strings por tamanho, organizando-as em ordem crescente de comprimento.

    Parâmetros:
    lista (list): Uma lista de strings a serem filtradas e organizadas.

    Retorna:
    list: A lista original e a lista ordenada por tamanho das strings.
    """
    lista_ordenada = sorted(lista, key=len)
    return lista, lista_ordenada

# Testando a função e imprimindo os resultados
lista_original, lista_ordenada = filtrar_por_tamanho(lista)
print("Lista original:", lista_original)
print("Lista organizada por tamanho de string:", lista_ordenada)

