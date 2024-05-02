# Criar um programa que simule a operação de dois grupos de amigos decidindo para quais filmes irão juntos ao cinema. Cada grupo tem sua própria lista de filmes preferidos (com possíveis duplicatas). O programa deve determinar quais filmes são comuns a ambos os grupos (interseção) e sugerir essas opções.

grupoA = ["filme1", "filme2", "filme3", "filme4", "filme5"]
grupoB = ["filme3", "filme4", "filme5", "filme6", "filme7"]

intersection_set = set(grupoA).intersection(set(grupoB))
print(intersection_set)