# Listagem de Números Primos
# Problema: Escreva um programa que verifique entre todos os números de 1 a 100 quais são números primos e exiba uma lista com todos.

def verificaPrimo(numero):
    """
    Verifica se um número é primo.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if numero <= 1:  # Se o número for menor ou igual a 1, não é primo
        return False
    
    for i in range(2, numero):  # Loop para verificar divisibilidade por números diferentes de 1 e o próprio número
        if numero % i == 0:  # Se for divisível por algum número diferente de 1 e ele mesmo, não é primo
            return False
    
    return True  # Se não for divisível por nenhum número diferente de 1 e ele mesmo, é primo

numeros_primos = []
for num in range(1, 101):
    if verificaPrimo(num):  # Se o número for primo, adiciona à lista de números primos
        numeros_primos.append(num)

print("Números primos de 1 a 100:")
print(numeros_primos)
