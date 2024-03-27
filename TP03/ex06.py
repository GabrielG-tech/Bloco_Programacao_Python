# Contador e classificador de caracteres
# Escreva um programa que receba uma string do usuário e retorne o número total de caracteres, de letras maiúsculas, letras minúsculas, números, caracteres especiais e barras de espaço desta string.

def contar_caracteres(string):
    """
    Conta e classifica os caracteres em uma string.

    Parâmetros:
    string (str): A string da qual os caracteres serão contados e classificados.

    Retorna:
    None
    """
    # Inicializando contadores
    total_caracteres = len(string)
    maiusculas = 0
    minusculas = 0
    numeros = 0
    especiais = 0
    espacos = 0
    
    # Iterando sobre cada caractere na string
    for caractere in string:
        if caractere.isupper():
            maiusculas += 1
        elif caractere.islower():
            minusculas += 1
        elif caractere.isdigit():
            numeros += 1
        elif caractere.isspace():
            espacos += 1
        else:
            especiais += 1
    
    # Imprimindo os resultados
    print("Total de caracteres:", total_caracteres)
    print("Letras maiúsculas:", maiusculas)
    print("Letras minúsculas:", minusculas)
    print("Números:", numeros)
    print("Caracteres especiais:", especiais)
    print("Espaços:", espacos)

entrada = input("Digite uma frase: ")

# Chamando a função para contar e classificar os caracteres
contar_caracteres(entrada)
