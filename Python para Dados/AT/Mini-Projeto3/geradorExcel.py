import pandas as pd

data = {
    'Usuário': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Jogos': [
        'The Witcher 3, Cyberpunk 2077, Minecraft',
        'Minecraft, Fortnite, Apex Legends',
        'The Witcher 3, Apex Legends, Stardew Valley',
        'The Witcher 3, Fortnite, Stardew Valley, Among Us',
        'Cyberpunk 2077, Among Us'
    ]
}

df = pd.DataFrame(data)
PATH = 'Python para Dados\\AT\\Mini-Projeto3\\consolidado_jogos.xlsx'

df.to_excel(PATH, index=False)
print(f"Arquivo Excel consolidado criado em: {PATH}")
