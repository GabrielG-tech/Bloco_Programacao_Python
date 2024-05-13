# Nivel 3 - Ex 1
# Fusão de Listas em Dicionário: Desenvolva um programa que combine duas listas, uma de chaves e outra de valores, em um único dicionário. Por exemplo, combine chaves = ['nome', 'idade'] com valores = ['Ana', 25] usando função nativa zip().

def listas_para_dicionario(chaves, valores):
    dicionario = dict(zip(chaves, valores))
    return dicionario

chaves = ['nome', 'idade']
valores = ['Ana', 25]

resultado = listas_para_dicionario(chaves, valores)
print("Dicionário resultante:", resultado)
