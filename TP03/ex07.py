# Gerador de Senha Aleatória
# Crie um programa que gere senhas aleatórias com letras (maiúsculas e minúsculas), números e símbolos, permitindo ao usuário especificar o comprimento da senha.

import random

def gerar_senha(comprimento):
    """
    Gera uma senha aleatória com letras (maiúsculas e minúsculas), números e símbolos.

    Argumentos:
    comprimento (int): O comprimento da senha a ser gerada.

    Retorna:
    str: A senha aleatória gerada.
    """
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()_+~`|}{[]:;?><,./-='
    senha = []
    
    senha.append(random.choice(letras_maiusculas))
    senha.append(random.choice(letras_minusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(simbolos))
    
    for _ in range(comprimento - 4):
        categoria = random.choice([letras_maiusculas, letras_minusculas, numeros, simbolos])
        senha.append(random.choice(categoria))
    
    # Embaralhando a senha
    random.shuffle(senha)
    
    # Convertendo a lista de caracteres em uma string e retornando a senha
    return ''.join(senha)

comprimento_senha = int(input("Digite o comprimento da senha desejada: "))
senha_gerada = gerar_senha(comprimento_senha)
print("A senha gerada é:", senha_gerada)
