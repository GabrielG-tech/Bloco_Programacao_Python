# Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.

min = float(input("Insira um número (em minutos): "))
hrs = min / 60
seg = min * 60
dia = (min / 60) / 24

print(round(min, 2), "minutos equivalem a" , round(dia, 3), "dias", round(hrs, 2), "horas", round(seg, 2), "segundos.")
