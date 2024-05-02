# Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.
escolha = ""
def apresentar_escolhas():
    print("\n" + "="*22 + " Bem-vindo à aventura " + "="*22)
    print("Você está em uma floresta misteriosa. Você encontra um caminho bifurcado.\n")
    print("Você deseja seguir para a esquerda ou para a direita?")

def escolher_caminho():
    escolha = input("Digite 'esquerda' ou 'direita' para fazer sua escolha: ").lower()
    if escolha == "esquerda":
        print("Você escolheu o caminho da esquerda.\n")
        resultado_esquerda()
    elif escolha == "direita":
        print("Você escolheu o caminho da direita.\n")
        resultado_direita()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        escolher_caminho()
    print("\n")

def resultado_esquerda():
    print("Você encontra uma cabana abandonada.")
    print("Deseja entrar na cabana ou continuar sua jornada?\n")

    escolha = input("Digite 'entrar' ou 'continuar': ").lower()
    if escolha == "entrar":
        print("Você encontra um baú cheio de tesouros. Parabéns, você venceu!")
    elif escolha == "continuar":
        print("Você continua sua jornada pela floresta.\n")
        continuar_jornada()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        resultado_esquerda()
    print("\n")

def resultado_direita():
    print("Você encontra um rio com uma ponte que parece instável.")
    print("Você deseja atravessar a ponte ou encontrar outra maneira de atravessar o rio?\n")

    escolha = input("Digite 'atravessar' ou 'encontrar': ").lower()
    if escolha == "atravessar":
        print("Você decide atravessar a ponte. Ela desaba e você cai no rio. Fim da jornada.\n")
    elif escolha == "encontrar":
        print("Você procura por outra maneira de atravessar o rio.\n")
        continuar_jornada()
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        resultado_direita()
    print("\n")

def continuar_jornada():
    print("Você continua sua jornada pela floresta.")
    print("Você avista uma caverna misteriosa à sua frente.")
    print("Deseja explorar a caverna ou continuar sua jornada pela floresta?\n")

    escolha = input("Digite 'explorar' ou 'continuar': ").lower()
    if escolha == "explorar":
        print("Você decide explorar a caverna.\n")
        resultado_caverna()
    elif escolha == "continuar":
        print("Você opta por continuar sua jornada pela floresta.")
        print("Infelizmente, ainda não implementamos mais desta parte da aventura!")
        print("Fim da jornada.")
    else:
        print("Opção inválida. Por favor, escolha novamente.")
        continuar_jornada()

def resultado_caverna():
    print("Você entra na caverna e encontra um tesouro escondido!")
    print("Parabéns, você venceu!")

while escolha != "atravessar" and escolha != "explorar" and escolha != "continuar":
    apresentar_escolhas()
    escolher_caminho()
    repetir = input("Deseja jogar novamente? (sim/não): ").lower()
    if repetir != "sim":
        break