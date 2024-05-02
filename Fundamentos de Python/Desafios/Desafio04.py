# Auto-média ou soma
# Escreva uma função que receba uma quantidade não definida de valores numéricos e, por padrão, retorne a média entre eles. Ou caso um argumento específico seja passado por uma palavra chave, ela retorne a soma entre estes números

lista = [4, 0, 0, 2, 8, 9, 2, 2]

def mediaSoma(*lista, soma=False):
    """
    Calcula a média ou a soma dos valores em uma lista.

    Parâmetros:
    lista (list): Uma lista de valores numéricos.
    soma (bool): Se True, calcula a soma dos valores. Se False (padrão), calcula a média.

    Retorna:
    float: A média dos valores se soma for False, a soma dos valores caso contrário.
    """
    resposta = 0
    if not lista:
        print("Não há uma lista declarada")
    else:
        if soma:
            for item in lista: resposta += item
        else:
            for item in lista: resposta += item
            resposta = resposta / len(lista)
        return resposta

print(f"A média de {lista} é {round(mediaSoma(lista), 2)}")
print(f"A soma de {lista} é {mediaSoma(lista, True)}")
