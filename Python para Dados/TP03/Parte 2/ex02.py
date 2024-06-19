# Crie uma função que recebe uma lista de números e retorna uma nova lista apenas com os números pares e positivos. Use uma classe de exceção personalizada para tratar o caso em que um número negativo seja encontrado, interrompendo a execução e retornando a lista acumulada até o ponto da exceção.

class ErroNumeroNegativo(Exception):
    def __init__(self, message="Número negativo encontrado."):
        self.message = message
        super().__init__(self.message)

def filtrar_pares_positivos(lista):
    """
    Filtra uma lista de números para retornar apenas os números pares e positivos.

    Args:
        lista: Lista contendo números inteiros.

    Returns:
        lista: Lista contendo apenas os números pares e positivos da lista de entrada.

    Raises:
        ErroNumeroNegativo: Se um número negativo for encontrado na lista, uma exceção é lançada indicando o número negativo encontrado e a execução é interrompida.
    """
    numeros_filtrados = []
    for num in lista:
        if num < 0:
            raise ErroNumeroNegativo(f"Número negativo encontrado: {num}")
        elif num % 2 == 0:
            numeros_filtrados.append(num)
    return numeros_filtrados

try:
    lista_numeros = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
    resultado = filtrar_pares_positivos(lista_numeros)
    print("Lista filtrada:", resultado)
except ErroNumeroNegativo as e:
    print("Erro:", e)
