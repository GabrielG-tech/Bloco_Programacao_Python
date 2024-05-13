# Nivel 1 - Ex 4
# Elabore um programa que leia um arquivo de texto, conte quantas palavras diferentes existem no texto e o número de ocorrências de cada uma e escreva os resultados em um novo arquivo de texto de forma ordenada por quantidade de aparições.

def contar_palavras(arquivo):
    contagem = {}
    palavras_distintas = 0
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            palavras = linha.lower().split()
            for palavra in palavras:
                palavra_limpa = ''.join(c for c in palavra if c.isalnum()) # Removendo tudo que não for letra ou número
                if palavra_limpa:
                    if palavra_limpa in contagem:
                        contagem[palavra_limpa] += 1
                    else:
                        contagem[palavra_limpa] = 1
                        palavras_distintas += 1
    return contagem, palavras_distintas

def salvar_resultados(contagem, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(f'Número de palavras distintas: {palavras_distintas}\n')
        # Organiza contagem pelo número de ocorrencias dentro, com o reverse fazendo a ordem ficar do maior para o menor
        for palavra, ocorrencias in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
            f.write(f'{palavra}: {ocorrencias}\n')

arquivo_entrada = "Python para Dados\\TP01\\Nivel1\\ex4.txt"
arquivo_saida = "Python para Dados\\TP01\\Nivel1\\ex4-resultado.txt"

contagem, palavras_distintas = contar_palavras(arquivo_entrada)
salvar_resultados(contagem, arquivo_saida)
print(f"Contagem de palavras salva com sucesso!\nNúmero de palavras distintas: {palavras_distintas}")
