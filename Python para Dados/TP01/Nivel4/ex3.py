# Nivel 4 - Ex 3
# Filtragem e Transformação em Sets: Escreva um programa que inicie com um set de números inteiros e, através de operações com sets, remova todos os números pares e, aos ímpares restantes, adicione 5. Exiba o set resultante.

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

impares = {num for num in numeros if num % 2 != 0}

resultado = {num + 5 for num in impares}

print(resultado)


