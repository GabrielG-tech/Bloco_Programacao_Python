# Conversor de Base Numérica
# Problema: Desenvolva um programa que converta um número da base decimal para binária usando um loop while.

#numero = int(input("Digite um número para conversão: "))
decimal = 39
test = 0
def decimal_para_binario(decimal):
    """
    Converte um número decimal para binário.

    Args:
    - decimal (int): O número decimal a ser convertido.

    Returns:
    - str: O número binário equivalente como uma string.
    """
    if decimal == 0:
        return '0'
        
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
        #print("Número:", decimal, "\tResto:", resto)
    return binario

# Solicita ao usuário o número decimal
numero_decimal = int(input("Digite um número decimal: "))

# Chama a função para converter o número e exibe o resultado
numero_binario = decimal_para_binario(numero_decimal)
print("O número binário equivalente é:", numero_binario)
