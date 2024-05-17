# Crie uma funcao que recebe uma lista de numeros e retorna uma nova lista apenas com os numeros positivos. Use uma excecao personalizada para tratar o caso em que um numero negativo e encontrado, interrompendo a execucao e retornando a lista acumulada ate o ponto da excecao.

lista = [1, 2, -3, -4, 5, 7, -10, -90]

class ErroNumeroNegativo(Exception):
    pass

def filtra_positivos(lista):
    lista_positivos = []
    try:
        for item in lista:
            if item >= 0:
                lista_positivos.append(item)
            else:
                raise ErroNumeroNegativo("Número negativo encontrado")
    except ErroNumeroNegativo as e:
        print(f"Tivemos o problema de {e}.")
    finally:
        return lista_positivos
        
print(lista)
lista_positivos = filtra_positivos(lista)
print("Lista resultante:", lista_positivos)

