import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4

url = 'https://pt.wikipedia.org/wiki/Rock'
resposta = requests.get(url)
# print(resposta.text)

# Utilizando BeautifulSoup para parsear o HTML
soup = BeautifulSoup(resposta.content, 'html.parser')

container = soup.find('div', class_='mw-content-ltr mw-parser-output')
h3 = soup.find_all('h3')
h4 = soup.find_all('h4')

for epoca in h3:
    genero = epoca.find('span', class_='mw-headline').get_text()  
    print(genero)
    # print(f'\n\033[1m{epoca}\033[0m:')

    for tipo in h4:
        batata = tipo.find('span', class_='mw-headline').get_text()    
        print("•", batata)

        