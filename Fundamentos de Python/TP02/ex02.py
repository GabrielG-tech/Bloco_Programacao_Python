# Acumulador de Soma
# Problema: Desenvolva um programa que use um loop while para somar todos os números até 100 e imprimir o resultado.

def soma(numero):
    """
    Esta função utiliza um loop while para somar todos os números até o número fornecido como argumento e retorna o resultado.

    Args:
    numero (int): O número até o qual se deseja somar.

    Returns:
    int: O resultado da soma dos números de 1 até o número fornecido.
    """
    contador = 0  # Inicia o contador em 0
    somatorio = 0  # Inicia o somatório em 0

    # Loop while para somar os números até o número fornecido
    while contador != numero:  # Enquanto o contador não alcançar o número fornecido
        contador += 1  # Incrementa o contador em 1 a cada iteração
        somatorio += contador  # Adiciona o valor do contador ao somatório

    return somatorio

# Imprime o resultado
print("A soma dos números de 1 até 100 é", soma(100))