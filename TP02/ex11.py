# Ordenador de Lista por Tamanho de Palavra
# Problema: Implemente um programa que organize uma lista de palavras em ordem crescente de tamanho.

lista = ["12345", "1234", "1234567", "12345", "12345678", "123456789", "123"]
lista_ordenada = sorted(lista, key=len)

print("Lista original:", lista)
print("Lista organizada:", lista_ordenada)
