# Validador de CPF
# Problema: Crie um programa que valide um número de CPF fornecido pelo usuário (considerando apenas a validação dos dígitos verificadores).

def validar_cpf(cpf):
    """
    Valida um número de CPF fornecido pelo usuário (considerando apenas a validação dos dígitos verificadores).

    Args:
    - cpf (str): O CPF a ser validado. Deve ser uma string contendo apenas os dígitos do CPF.

    Returns:
    - bool: Retorna True se o CPF for válido (os dígitos verificadores estiverem corretos), False caso contrário.
    """

    cpf = ''.join(filter(str.isdigit, cpf))  # Remover caracteres não numéricos

    if len(cpf) != 11 or cpf == cpf[0] * 11:  # Verificar se o CPF tem 11 dígitos e não é uma sequência repetida
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))  # Calculando o primeiro dígito verificador
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))  # Calculando o segundo dígito verificador
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])  # Verificando se os dígitos calculados coincidem com os dígitos fornecidos

# Exemplo de uso
cpf = input("Digite o CPF (somente números): ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
