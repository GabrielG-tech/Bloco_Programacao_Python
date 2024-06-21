from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd

PATH = 'Python para Dados\\AT\\ProjetoIntegrador\\'

engine = create_engine(f'sqlite:///{PATH}/banco_jogos.db')

# Criar base de dados
Base = declarative_base()

class Consoles(Base):
    __tablename__ = 'consoles'
    id = Column(Integer, primary_key=True)
    console = Column(String)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    data_nascimento = Column(String)
    email = Column(String)
    cidade = Column(String)

class UsuarioConsole(Base):
    __tablename__ = 'usuario_console'
    id = Column(Integer, primary_key=True)
    usuario = Column(Integer, ForeignKey('usuarios.id'))
    idConsole = Column(Integer, ForeignKey('consoles.id'))

class JogosMercadoLivre(Base):
    __tablename__ = 'jogos_mercado_livre'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    preco = Column(Float)
    permalink = Column(String)

class JogosPreferidos(Base):
    __tablename__ = 'jogos_preferidos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

# Criar tabelas:
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Função para importar dados de CSV e inserir no banco de dados
def importar_dados(csv_path, dados):
    data = pd.read_csv(csv_path)
    try:
        data.to_sql(dados, con=engine, if_exists='append', index=False)
        print(f'Dados importados para a tabela {dados} com sucesso.')
    except Exception as e:
        print(f'Erro ao importar dados para a tabela {dados}: {e}')

# Função para exportar dados do banco de dados para CSV
def exportar_dados(table, export_path):
    try:
        df = pd.read_sql_table(table, con=engine)
        df.to_csv(export_path, index=False)
        print(f'Dados exportados da tabela {table} para {export_path} com sucesso.')
    except Exception as e:
        print(f'Erro ao exportar dados da tabela {table}: {e}')

PATH = 'Python para Dados\\AT\\ProjetoIntegrador\\'
PATH_1 = 'Python para Dados\\AT\\Mini-Projeto1\\Arquivos_Exportados\\'
PATH_2 = 'Python para Dados\\AT\\Mini-Projeto2\\usuarios-consolidados.xlsx'

# Converter Excel para CSV e importar dados
usuarios_excel = pd.read_excel(PATH_2)
csv_path = f'{PATH}Arquivos_Exportados\\usuarios_consolidados.csv'
usuarios_excel.to_csv(csv_path, index=False)
importar_dados(csv_path, 'usuarios')

PATH_3 = 'Python para Dados\\AT\\Mini-Projeto3\\banco_de_dados.sqlite' # consultar e pegar valores da coluna "Jogo" da tabela "jogos_separados"

# Importar dados do outro banco SQLite
engine_2 = create_engine(f'sqlite:///{PATH_3}')
jogos_df = pd.read_sql_table('jogos_separados', con=engine_2, columns=['Jogo'])
jogos_df.columns = ['nome']
jogos_df.to_sql('jogos_preferidos', con=engine, if_exists='append', index=False)
print('Dados importados da tabela jogos_separados para jogos_preferidos com sucesso.')

PATH_4 = 'Python para Dados\\AT\\Mini-Projeto4\\mercado_livre.db' # consultar e pegar a coluna "nome" e "preço" da tabela "jogos_mercado_livre"

# Importar dados do outro banco
engine_3 = create_engine(f'sqlite:///{PATH_4}')
jogos_mercado_livre_df = pd.read_sql_table('jogos_mercado_livre', con=engine_3, columns=['nome', 'preco'])
jogos_mercado_livre_df.to_sql('jogos_mercado_livre', con=engine, if_exists='replace', index=False)
print('Dados importados da tabela jogos_mercado_livre para jogos_mercado_livre com sucesso.')

# Exportar dados para arquivos CSV
export_paths_and_tables = [
    (f'{PATH}Arquivos_Exportados\\exported_jogos_mercado_livre.csv', 'jogos_mercado_livre'),
    (f'{PATH}Arquivos_Exportados\\exported_jogos_preferidos.csv', 'jogos_preferidos'),
]

for export_path, table_name in export_paths_and_tables:
    exportar_dados(table_name, export_path)

# Recomendação dos 5 jogos mais baratos
def recomendar_jogos_mais_baratos():
    try:
        jogos_mais_baratos = session.query(JogosMercadoLivre).order_by(JogosMercadoLivre.preco).limit(5).all()
        print("Recomendação dos 5 jogos mais baratos são:")
        for jogo in jogos_mais_baratos:
            print(f"Nome: {jogo.nome}, Preço: R${jogo.preco:.2f}, Link: {jogo.permalink}")
    except Exception as e:
        print(f"Erro ao buscar os jogos mais baratos: {e}")

# Chamando a função de recomendação dos 5 jogos mais baratos
recomendar_jogos_mais_baratos()
