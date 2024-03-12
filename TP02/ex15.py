# Função Geradora de Senhas Aleatórias
# Problema: Escreva uma função que gere uma senha aleatória contendo letras maiúsculas, minúsculas, números e símbolos.

import random

def gerarSenha(numCaracteres=8):
    """
    Gera uma senha aleatória contendo letras maiúsculas, minúsculas, números e símbolos.

    Args:
    - numCaracteres (int): O número de caracteres que a senha deve conter. O padrão é 8.

    Returns:
    - senha (str): A senha gerada.
    """

    # Conjuntos de caracteres possíveis para a senha
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%&*()_+-=[]{}|;:,.<>?'

    # Concatenando todos os conjuntos de caracteres em uma única string
    caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    # Gerando a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(numCaracteres))

    return senha

# Exemplo de uso
senha = gerarSenha(12)  # Gerar senha com 12 caracteres
print(senha)
