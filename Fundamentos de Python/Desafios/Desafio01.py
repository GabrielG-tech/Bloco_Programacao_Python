# • Utilizar operadores aritméticos para criar um programa em Python que calcule e informe quantos dias, semanas, horas, minutos e segundos tem esse curso.

# • Dados:
# • São 11 semanas de curso.
# • 2 aulas por semana.
# • Cada aula 2 horas e meia.
# • Sendo que 1 feriado cai na sexta-feira.

numero_de_encontros = 11 * 2 - 1
horas_de_curso = numero_de_encontros * 2.5
minutos_de_curso = horas_de_curso * 60
segundos_de_curso = minutos_de_curso * 60
dias_de_curso = horas_de_curso / 24
semanas_de_curso = dias_de_curso / 7

print("Duração do curso:")
print("\tDias:", dias_de_curso)
print("\tSemanas:", semanas_de_curso)
print("\tHoras:", horas_de_curso)
print("\tMinutos:", minutos_de_curso)
print("\tSegundos:", segundos_de_curso)
