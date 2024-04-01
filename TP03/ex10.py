# Codificador/Decodificador de Mensagens
# Implemente um script que use uma cifra de substituição simples (como a cifra de César) para codificar e decodificar mensagens.

def codificar_mensagem(mensagem, chave):
    """
    Codifica uma mensagem usando a cifra de César.

    Argumentos:
        mensagem (str): A mensagem a ser codificada.
        chave (int): O número de posições para deslocar no alfabeto.

    Retorna:
        str: A mensagem codificada.
    """
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem_codificada = ''
    for caractere in mensagem:
        if caractere.isalpha():
            indice = alfabeto.index(caractere)
            novo_indice = (indice + chave) % len(alfabeto)
            novo_caractere = alfabeto[novo_indice]
            mensagem_codificada += novo_caractere
        else:
            mensagem_codificada += caractere
    return mensagem_codificada

def decodificar_mensagem(mensagem_codificada, chave):
    """
    Decodifica uma mensagem previamente codificada com a cifra de César.

    Argumentos:
        mensagem_codificada (str): A mensagem codificada.
        chave (int): O número de posições para deslocar no alfabeto.

    Retorna:
        str: A mensagem decodificada.
    """
    return codificar_mensagem(mensagem_codificada, -chave)

# Entrada da mensagem pelo usuário
mensagem_original = input("Digite a mensagem: ")
chave = int(input("Digite a chave de codificação (um número inteiro): "))

# Codificar a mensagem
mensagem_codificada = codificar_mensagem(mensagem_original, chave)
print("Mensagem codificada:", mensagem_codificada)

# Decodificar a mensagem
mensagem_decodificada = decodificar_mensagem(mensagem_codificada, chave)
print("Mensagem decodificada:", mensagem_decodificada)
