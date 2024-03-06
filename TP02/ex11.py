# Ordenador de Lista por Tamanho de Palavra
# Problema: Implemente um programa que organize uma lista de palavras em ordem crescente de tamanho.

lista = ["12345", "1234", "1234567", "12345", "12345678", "123456789", "123"]
lista_ordenada = []

print("Lista original:", lista)

for i in range(len(lista) - 1):
    for i in range(len(lista) - 1):  # Loop por indice
        if len(lista[i]) > len(lista[i + 1]):
            lista_ordenada.append(lista[i + 1])
            lista_ordenada.append(lista[i])
    print("Lista filtrada 1ºvez:", lista_ordenada)
    lista = lista_ordenada
    lista_ordenada = []

print("Lista filtrada muitas vezes:", lista_ordenada)