# Nivel 4 - Ex 3
# Filtragem e Transformação em Sets: Escreva um programa que inicie com um set de números inteiros e, através de operações com sets, remova todos os números pares e, aos ímpares restantes, adicione 5. Exiba o set resultante.

# Inicializa um conjunto de números inteiros
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Filtra os números pares
impares = {num for num in numeros if num % 2 != 0}

# Adiciona 5 aos números ímpares
resultado = {num + 5 for num in impares}

# Exibe o conjunto resultante
print(resultado)
