# Escreva um código que tenta abrir e ler um arquivo chamado config.yaml. Se o arquivo não for encontrado, crie-o com conteúdo padrão (config: default) e exiba uma mensagem informando a criação do arquivo.

import yaml # pip install pyyaml
import os

def ler_configuracao():
    """
    Tenta abrir e ler um arquivo chamado "config.yaml", se o arquivo não for encontrado, ele é criado com um conteúdo padrão ("config: default")
    """
    arquivo_config = 'config.yaml'
    PATH = "Python para Dados\\TP03\\Parte 2\\" + arquivo_config

    if os.path.exists(PATH):
        with open(PATH, 'r') as file:
            try:
                configuracoes = yaml.safe_load(file)
                print("Configurações encontradas:", configuracoes)
            except yaml.YAMLError as e:
                print(f"Erro ao ler o arquivo {PATH}: {e}")
    else:
        # se o arquivo não existir é criado com um conteúdo padrão
        configuracoes = {'config': 'default'}
        with open(PATH, 'w') as file:
            yaml.safe_dump(configuracoes, file)
        print(f"Arquivo {arquivo_config} criado com sucesso.")
ler_configuracao()
