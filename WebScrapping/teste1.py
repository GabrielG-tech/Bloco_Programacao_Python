import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4

url = 'https://pt.wikipedia.org/wiki/Rock'
resposta = requests.get(url)
# print(resposta.text)

# Utilizando BeautifulSoup para parsear o HTML
soup = BeautifulSoup(resposta.content, 'html.parser')

# Extraindo o titulo da pagina
titulo = soup.title.text
print('Titulo da pagina:', titulo)
