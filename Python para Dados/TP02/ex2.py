# Crie um programa que simule a operação de dois grupos de amigos decidindo para quais filmes irão juntos ao cinema:
# A. Cada grupo tem sua própria lista de filmes preferidos (com possíveis duplicatas).
# B. O programa deve determinar quais filmes são comuns a ambos os grupos (interseção) e sugerir essas opções.

def filmes_comuns(grupo1, grupo2):
    conjunto_grupo1 = set(grupo1)
    conjunto_grupo2 = set(grupo2)
    filmes_comuns = conjunto_grupo1.intersection(conjunto_grupo2)
    
    return list(filmes_comuns)

grupo1_filmes = ["Matrix", "Vingadores", "Star Wars", "Matrix", "Homem-Aranha"]
grupo2_filmes = ["Star Wars", "Vingadores", "Avatar", "Matrix", "Matrix"]

filmes_sugeridos = filmes_comuns(grupo1_filmes, grupo2_filmes)
print("Filmes comuns sugeridos:", filmes_sugeridos)
