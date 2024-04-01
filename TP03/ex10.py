# Codificador/Decodificador de Mensagens
# Implemente um script que use uma cifra de substituição simples (como a cifra de César) para codificar e decodificar mensagens.

def codificar_mensagem(mensagem, chave):
    """
    Codifica uma mensagem usando a cifra de César.

    Argumentos:
        mensagem (str): Uma mensagem a ser codificada.
        chave (int): O número de posições para deslocar no alfabeto.

    Retorna:
        str: Mensagem codificada.
    """
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mensagem_codificada = ''

    for caractere in mensagem:
        if caractere.isalpha():
            # Método da Cifra de César
            indice = alfabeto.index(caractere)
            # Aplica a mudança com base na chave e o módulo (%) garante que o indice não ultrapasse o limite de caracteres de alfabeto.
            novo_indice = (indice + chave) % len(alfabeto)
            novo_caractere = alfabeto[novo_indice]
            mensagem_codificada += novo_caractere
        else:
            # Caso haja elementos que não sejam letras ele sera adicionando na mesma posição de origem
            mensagem_codificada += caractere
    return mensagem_codificada

def decodificar_mensagem(mensagem_codificada, chave):
    """
    Decodifica uma mensagem que já foi codificada com a cifra de César.

    Argumentos:
        mensagem_codificada (str): Uma mensagem codificada.
        chave (int): O número de posições para deslocar no alfabeto.

    Retorna:
        str: Uma mensagem decodificada.
    """
    return codificar_mensagem(mensagem_codificada, -chave)

mensagem = input("Digite a mensagem: ")

while True:
    chave = int(input("Digite a chave de codificação (um número inteiro): "))
    if chave is int: break
    else: print("A chave deve ser um número inteiro.")

mensagem_codificada = codificar_mensagem(mensagem, chave)
print("Mensagem codificada:", mensagem_codificada)

mensagem_decodificada = decodificar_mensagem(mensagem_codificada, chave)
print("Mensagem decodificada:", mensagem_decodificada)
