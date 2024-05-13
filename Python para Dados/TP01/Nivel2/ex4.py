# Nivel 2 - Ex 4
# Conversão de Listas para Dicionários: Escreva um programa que leia uma lista de tuplas, onde cada tupla contém o nome de aluno e sua nota (exemplo: [("Ana", 8), ("João", 7)]), e a converta em um dicionário.

def lista_para_dicionario(lista):
    dicionario = {}
    for nome, nota in lista:
        dicionario[nome] = nota
    return dicionario

lista_de_notas = [("Ana", 8), ("João", 7), ("Maria", 9)]
dicionario_de_notas = lista_para_dicionario(lista_de_notas)
print(dicionario_de_notas)
