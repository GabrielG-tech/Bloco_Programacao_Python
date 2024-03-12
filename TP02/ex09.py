# Função de Fatorial
# Problema: Escreva uma função que calcule o fatorial de um número passado como argumento e retorne o resultado.

def fatorial(n):
    """
    Calcula o fatorial de um número inteiro não negativo.

    Args:
        n (int): O número para o qual o fatorial será calculado.

    Returns:
        int: O fatorial de n.
    """
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando a função
numero = int(input("Digite um número para calculo de fatorial: "))
resultado = fatorial(numero)

# Formatando o resultado com separadores de milhar
resultado_formatado = "{:,}".format(resultado).replace(",", ".")
print(f"O fatorial de {numero} é {resultado_formatado}.")