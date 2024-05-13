# Nivel 2 - Ex 3
# Operações com Sets: Escreva um programa que leia dois sets, identifique e exiba para o usuário a interseção e a união desses sets.

set1 = set(input("Insira os elementos do primeiro set separados por espaço: ").split())
set2 = set(input("Insira os elementos do segundo set separados por espaço: ").split())

# Calculando a interseção e a união
intersection = set1.intersection(set2)
union = set1.union(set2)

print("Interseção dos sets:", intersection) # Somente o que ambos tem em comum
print("União dos sets:", union) # O somatorio dos dois sem que haja repetição
