# "Calculadora de Viagem": Crie um programa em Python que pergunte ao usuário a distância de uma viagem em quilômetros e a velocidade média esperada para a viagem. O programa deve calcular e exibir o tempo aproximado da viagem em horas e minutos.

# Objetivo do Desafio: Este desafio visa aplicar os conceitos de entrada de dados, operações matemáticas e conversão de unidades (de km/h para horas e minutos), pensando de forma lógica e prática.

# Dicas:

# - Lembre-se de converter a distância para tempo usando a velocidade.
# - Divida o resultado para obter horas e o resto para obter minutos.
# - Teste o programa com diferentes entradas para garantir a precisão.

distancia = float(input("Digite a distância da viagem (km): "))

velocidade_media = float(input("Digite a velocidade média esperada para a viagem (km/h): "))

tempo_de_viagem_horas = distancia / velocidade_media

tempo_de_viagem_minutos = (tempo_de_viagem_horas - int(tempo_de_viagem_horas)) * 60

print("A viagem durará em média", int(tempo_de_viagem_horas), "horas e", int(tempo_de_viagem_minutos), "minutos.")