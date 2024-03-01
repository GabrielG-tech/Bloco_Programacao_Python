# Função de Potência Customizada
# Problema: Escreva uma função que calcule a potência de um número com um expoente padrão de 2, permitindo ao usuário alterar esse expoente com parâmetros por Keyword e retorne o resultado da operação.

def potencia(base, expoente=2):
    """
    Calcula a potência de um número com um expoente padrão de 2.

    Args:
        base (float): O número base.
        expoente (float, optional): O expoente para o qual a base será elevada.
            Padrão é 2.

    Returns:
        float: O resultado da operação de potência.

    """
    return base ** expoente

# Testando a função
base = 3
expoente = 4
resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é {resultado}.")

# Testando a função com o expoente padrão
resultado_padrao = potencia(base)
print(f"{base} elevado ao expoente padrão é {resultado_padrao}.")
