# Nivel 3 - Ex 3
# Sets com Condições: Implemente um programa que receba do usuário nomes de cidades e os adicione a um set, apenas se eles não estiverem presentes em um dicionário pré-definido que contém os estados como chaves e as suas capitais como valor. Use boas práticas para tratar a entrada do usuário.

capitais = {
    'São Paulo': 'São Paulo',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Minas Gerais': 'Belo Horizonte'
}

def adicionar_cidade(set_cidades, dicionario_capitais):
    while True:
        cidade = input("Digite o nome da cidade (ou 'sair' para encerrar): ").strip().title()
        
        if cidade.lower() == 'sair':
            break
        
        estado = input("Digite o nome do estado ao qual a cidade pertence: ").strip().title()

        # Analisa se a cidade já está presente em uma das capitais dos estados
        if estado in dicionario_capitais and cidade not in dicionario_capitais[estado]:
            set_cidades.add(cidade)
            print(f"{cidade} adicionada ao set de cidades.")
        elif estado not in dicionario_capitais:
            print(f"O estado '{estado}' não está na lista de estados e capitais.")
        else:
            print(f"{cidade} já é a capital de {estado}.")

cidades = set()
adicionar_cidade(cidades, capitais)

print("Cidades adicionadas:", cidades)
