# Crie uma lista aleatória e usando list comprehensions remova todos multiplos de 5 desta lista e exiba ela.

import random

# Criando uma lista aleatória de números inteiros
lista_aleatoria = [random.randint(1, 100) for _ in range(20)]

# Removendo os múltiplos de 5 da lista usando list comprehension
lista_sem_multiplos_de_5 = [num for num in lista_aleatoria if num % 5 != 0]

# Exibindo a lista resultante
print("Lista aleatória original:", lista_aleatoria)
print("Lista sem múltiplos de 5:", lista_sem_multiplos_de_5)
