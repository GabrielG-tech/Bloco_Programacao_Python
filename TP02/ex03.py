# Concatenação e Organizador de Listas
# Problema: Crie um programa que concatene duas listas fornecidas pelo usuário e organize a lista em ordem crescente.

def concatenarOrganizar(lista1, lista2):
    """
    Concatena duas listas fornecidas e organiza a lista resultante em ordem crescente.

    Args:
        lista1 (list): A primeira lista a ser concatenada.
        lista2 (list): A segunda lista a ser concatenada.

    Returns:
        list: A lista resultante da concatenação e organização das duas listas em ordem crescente.
    """
    # Concatena as duas listas
    lista1.extend(lista2)
    # Ordena a lista resultante em ordem crescente
    lista1.sort()
    return lista1

# Listas fornecidas pelo usuário
lista1 = []
lista2 = []

# Loop para inserir elementos na lista1
for i in range(1, 5):
    lista1.append(int(input("Digite um número para lista 1: ")))
    
# Loop para inserir elementos na lista2
for i in range(1, 5):
    lista2.append(int(input("Digite um número para lista 2: ")))

# Chama a função para concatenar e organizar as listas
resultado = concatenarOrganizar(lista1, lista2)

# Imprime o resultado
print(resultado)
