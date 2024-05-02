# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

n = int(input("Insira um número (em minutos): "))

h = n / 60
m = n - (60 * h)

if m < 10: m = "0" + str(m)

print(str(n) + "min = " + str(h) + "h" + str(m))