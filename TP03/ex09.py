# Validador de Senhas
# Crie um script que valide e classifique a complexidade de uma senha baseado em critérios definidos (ex: mínimo de caracteres maiúsculos e minúsculos, uso de números e símbolos).

def validar_senha(senha):
    """
    Valida a complexidade de uma senha com base em critérios definidos.

    Argumentos:
        senha (str): A senha a ser validada.

    Retorna:
        str: Uma string indicando a complexidade da senha. Pode ser "Senha forte" se a senha atender a todos os critérios definidos,
             ou "Senha fraca" caso contrário.
    """

    # Definindo critérios
    comprimento_minimo = 8
    possui_maiuscula = False
    possui_minuscula = False
    possui_numero = False
    possui_caracter_especial = False
    caracteres_especiais = "!@#$%^&*(),.?\":{}|<>"

    # Verifica cada caractere da senha
    for char in senha:
        if char.isupper():
            possui_maiuscula = True
        elif char.islower():
            possui_minuscula = True
        elif char.isdigit():
            possui_numero = True
        elif char in caracteres_especiais:
            possui_caracter_especial = True
    
    # Verificando se atende a todos os critérios
    if (len(senha) >= comprimento_minimo):
        if (possui_maiuscula and possui_minuscula and possui_numero and possui_caracter_especial):
            return "Senha forte"
    else:
        return "Senha fraca"

# Exemplo de uso
senha = input("Digite sua senha: ")
resultado = validar_senha(senha)
print("Complexidade da senha:", resultado)
