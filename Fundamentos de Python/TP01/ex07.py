# Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

# IMC = peso (kg) / altura^altura (m)

continuar = "s"
while (continuar != "n" ):
    peso = float(input("\nDigite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    IMC = peso / altura**altura

    print("\nSeu IMC é", round(IMC, 2))

    if (IMC <= 18.5): 
        print("Você está abaixo do peso")
    elif (18.6 <= IMC <= 24.9): 
        print("Você está no peso ideal (parabéns)")
    elif (25.0 <= IMC <= 29.9): 
        print("Você está levemente acima do peso")
    elif (30.0 <= IMC <= 34.9): 
        print("Você está com obesidade grau I")
    elif (35.0 <= IMC <= 39.9): 
        print("Você está com obesidade grau II (severa)")
    elif (IMC <= 40.0): 
        print("Você está com obesidade III (mórbida)")
    continuar = input("\nDeseja recalcular seu IMC? (s/n): ")
