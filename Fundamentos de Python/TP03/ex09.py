# Validador de Senhas
# Crie um script que valide e classifique a complexidade de uma senha baseado em critérios definidos (ex: mínimo de caracteres maiúsculos e minúsculos, uso de números e símbolos).

def validar_senha(senha):
    """
    Valida a complexidade de uma senha de acordo com critérios definidos.

    Argumentos:
        senha (str): A senha a ser validada.

    Retorna:
        str: uma string "Senha forte" se a senha atender a todos os critérios definidos,
        ou "Senha fraca" caso não atenda todos os critérios. Sendo eles: comprimento mínimo de 8 caracteres, pelo menos uma letra maiúscula, pelo menos uma letra minúscula, pelo menos um número e pelo menos um símbolo.
    """

    # Critérios:
    comprimento_minimo = 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False

    if len(senha) < comprimento_minimo:
        return "Senha fraca, a senha deve ter pelo menos 8 caracteres."

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif not caractere.isalnum():
            tem_simbolo = True
    
    if not tem_maiuscula:
        return "Senha fraca, a senha deve conter pelo menos uma letra maiúscula."
    elif not tem_minuscula:
        return "Senha fraca, a senha deve conter pelo menos uma letra minúscula."
    elif not tem_numero:
        return "Senha fraca, a senha deve conter pelo menos um número."
    elif not tem_simbolo:
        return "Senha fraca, a senha deve conter pelo menos um símbolo."
    else:
        return "Senha forte"

while True:
    senha = input("Digite uma senha: ")
    resultado = validar_senha(senha)
    print(resultado)
    if resultado == "Senha forte":
        break
