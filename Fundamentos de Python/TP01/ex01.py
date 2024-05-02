# Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.

n1 = float(input("Insira o 1º número: "))
n2 = float(input("Insira o 2º número: "))

print("\nSoma: " + str(n1 + n2))
print("Subtração: " + str(n1 - n2))
print("Multiplicação: " + str(n1 * n2))
print("Divisão Decimal: " + str(n1 / n2))
print("Divisão Inteira: " + str(int(n1 / n2)))