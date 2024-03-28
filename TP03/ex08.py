# Substituidor de Palavras em Texto
# Escreva um programa que substitua todas as ocorrências de uma palavra específica em um texto por outra palavra fornecida pelo usuário.

def substituir_palavra(texto, palavra_antiga, palavra_nova):
    """
    Substitui todas as ocorrências de uma palavra específica em um texto por outra palavra.

    Parâmetros:
    texto (str): O texto no qual as substituições serão feitas.
    palavra_antiga (str): A palavra a ser substituída.
    palavra_nova (str): A palavra que substituirá a palavra antiga.

    Retorna:
    str: O texto com todas as substituições feitas.
    """
    return texto.replace(palavra_antiga, palavra_nova)

texto = input("Digite o texto: ")
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a nova palavra: ")

texto_modificado = substituir_palavra(texto, palavra_antiga, palavra_nova)
print("Texto modificado:")
print(texto_modificado)
