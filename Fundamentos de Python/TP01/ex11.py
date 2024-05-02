# Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random 

numero_de_dados = int(input("Digite o número de dados a serem lançados: "))

lados_do_dado = [1, 2, 3, 4, 5, 6]
resultados = []

for i in range(numero_de_dados):
    resultados.append(random.choice(lados_do_dado))

print("Seus resultados foram", resultados)