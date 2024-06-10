# Utilizando JSON com uma API, escreva um programa que faça uma requisição à API “cep.awesomeapi.com.br” passando o CEP de um endereço no Brasil conhecido por você e exiba na tela o nome da rua, avenida ou travessa em questão, a cidade e o estado deste CEP.

import requests

def info_cep(cep):
    url = f"https://cep.awesomeapi.com.br/json/{cep}"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        rua = dados.get('address')
        cidade = dados.get('city')
        estado = dados.get('state')
        
        return rua, cidade, estado
    else:
        return None, None, None

cep = "20520050"  # Exemplo: CEP da Academia Escola Pico
rua, cidade, estado = info_cep(cep)

if rua and cidade and estado:
    print(f"Rua: {rua}\nCidade: {cidade}\nEstado: {estado}")
else:
    print("CEP não encontrado ou inválido.")
