# Conversor de Números Romanos
# Faça um programa que converta um número romano para um número decimal e vice-versa.

def romano_para_decimal(romano):
    """
    Converte um número romano para decimal.

    Parâmetros:
    romano (str): O número romano a ser convertido.

    Retorna:
    int: O valor decimal equivalente ao número romano fornecido.
    """
    algarismos_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    valor_anterior = 0
    for algarismo in romano[::-1]:
        if algarismo not in algarismos_romanos:
            print("O número em romano tem caracter(es) inválido(s).")
            exit()
        valor = algarismos_romanos[algarismo]
        if valor < valor_anterior:
            decimal -= valor
        else:
            decimal += valor
        valor_anterior = valor
    return decimal


def decimal_para_romano(decimal):
    """
    Converte um número decimal para romano.

    Parâmetros:
    decimal (int): O número decimal a ser convertido.

    Retorna:
    str: O número romano equivalente ao valor decimal fornecido.
    """
    mapa_decimal_romano = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    romano = ''
    for valor, algarismo in mapa_decimal_romano:
        while decimal >= valor:
            romano += algarismo
            decimal -= valor
    return romano

while True:
    try:
        escolha = input("Digite [R] para converter um número romano para decimal ou [D] para converter um número decimal para romano: ").upper()
        if escolha == 'R':
            numero_romano = input("Digite o número romano que deseja converter para decimal: ").upper()
            valor_decimal = romano_para_decimal(numero_romano)
            print(f'O número romano {numero_romano} é equivalente a {valor_decimal} em decimal.')
        elif escolha == 'D':
            numero_decimal = int(input("Digite o número decimal que deseja converter para romano: "))
            if numero_decimal <= 0:
                raise ValueError("Entrada inválida: o número decimal deve ser maior que zero.")
            numero_romano = decimal_para_romano(numero_decimal)
            print(f'O número decimal {numero_decimal} é equivalente a {numero_romano} em romano.')
        else:
            print("Opção inválida. Por favor, escolha 'R' ou 'D'.")
        break
    except ValueError:
        print("Você inseriu um caractere inválido. Por favor, tente novamente...")
