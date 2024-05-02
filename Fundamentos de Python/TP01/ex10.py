# Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.

import random

personagens = [
    "Harry Potter",
    "Bilbo Baggins",
    "Aragorn",
    "Katniss Everdeen",
    "Sherlock Holmes",
    "Elizabeth Bennet",
    "Atticus Finch",
    "Frodo Baggins",
    "Hermione Granger",
    "Jon Snow"
]

ações = [
    "encontrou um mapa do tesouro",
    "descobriu uma nova espécie de borboleta",
    "ganhou um prêmio de ciências",
    "fez uma viagem ao redor do mundo",
    "criou uma obra de arte que foi exibida em uma galeria famosa"]

locais = [
    "em uma ilha deserta",
    "nas profundezas da floresta",
    "em uma cidade subterrânea",
    "em uma montanha flutuante",
    "em uma dimensão paralela"]

personagem = random.choice(personagens)
ação = random.choice(ações)
local = random.choice(locais)

historia = f"{personagem} {ação} {local}."

print(historia)