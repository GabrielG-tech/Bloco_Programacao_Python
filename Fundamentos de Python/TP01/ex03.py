# Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome.

n1 = input("Insira o 1º nome: ")
n2 = input("Insira o 2º nome: ")

n1 = n1[0:int(len(n1)/2)]
n2 = n2[int(len(n2)/2):]

print(n1 + n2)