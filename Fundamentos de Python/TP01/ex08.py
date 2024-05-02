# Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

idade = int(input("Digite sua idade: "))

if (idade > 18):
    print("Você é maior de idade!)")
elif (idade == 18):
    print("Parabéns você já é maior de idade! (Está na hora de renovar a identidade)")
elif (idade < 18):
    print("Você ainda não é maior de idade (aproveite enquanto não tem que pagar inposto!)")