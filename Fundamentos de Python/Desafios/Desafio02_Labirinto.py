# "O Jogo do Labirinto”

# Descrição: Crie um programa que simula um pequeno labirinto. O usuário deve escolher direções (esquerda, direita, frente) para encontrar a saída. O programa deve informar se o usuário está se aproximando ou se afastando da saída.

# Dica: O jogo pode considerar o caminho apenas como um posição específica numa reta numérica e as ações esquerda, direta e frente serem apenas operações matemáticas desconhecidas do usuário.

print("\n" + "="*12 + " Bem-Vindo ao meu Labirinto! " + "="*12)
print("Se esforce para achar a saída!!!\n• Escolha uma das opções mostradas para continuar o jogo:")
print("[E] - Virar a Esquerda\n[D] - Virar a Direita\n[F] - Seguir em Frente\n")

posicao_atual = 0 # Início do labirinto
posicao_anterior = 0
destino = 10 
passos = 0 # Contador de jogadas

while (posicao_atual != destino):
    escolha = input("> ").upper()

    if escolha not in ['E', 'D', 'F']:
        print("Escolha inválida. Tente novamente.")
        continue 

    if escolha == "E":
        posicao_atual -= 1
        print("Você virou a esquerda") 
    elif escolha == "D":
        posicao_atual += 1
        print("Você virou a direita") 
    elif escolha == "F":
        posicao_atual += 2
        print("Você seguiu em frente") 

    distancia = abs(destino - posicao_atual)
    passos += 1

    if abs(destino - posicao_atual) < abs(destino - posicao_anterior):
        print(f"Você está se aproximando da saída. Distância: {distancia} unidades.")
    else:
        print(f"Você está se afastando da saída. Distância: {distancia} unidades.")
    
print(f"Parabéns! Você encontrou a saída do labirinto em {passos} passos!")
