import json
import re
import pandas as pd
from datetime import datetime

# Caminho dos arquivos
csv_file = 'Python para Dados\\AT\\Mini-Projeto2\\DadosAnalisados\\dadosAT.csv'
json_file = 'Python para Dados\\AT\\Mini-Projeto2\\DadosAnalisados\\dadosATAntigo.json'
excel_file = 'Python para Dados\\AT\\Mini-Projeto2\\DadosAnalisados\\dadosATAntigo.xlsx'

def ler_arquivos(csv_path, json_path, excel_path):
    try:
        df_csv = pd.read_csv(csv_path)

        with open(json_path) as f:
            json_data = json.load(f)
        df_json = pd.DataFrame(json_data)

        df_excel = pd.read_excel(excel_path)
        return df_csv, df_json, df_excel
    except Exception as e:
        print(f"Erro ao ler arquivos: {e}")
        return None, None, None
    
def formatar_data(data):
    try:
        # Verifica se a data está no formato dd/mm/yyyy ou dd-mm-yyyy
        if '/' in data:
            data = data.replace('/', '-')
        
        # Verifica se a data está no formato dd-mm-yyyy
        match = re.match(r'(\d{2})-(\d{2})-(\d{4})', data)
        if match:
            return f"{match.group(3)}-{match.group(2)}-{match.group(1)}"
        else:
            return data
    except Exception as e:
        print(f"Erro ao formatar data: {e}")
        return data

def validar_email(email):
    # Expressão regular para validar o formato do email
    regex_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.match(regex_email, email)

def limpar_dados(df):
    try:
        df.drop_duplicates(inplace=True)
        df.fillna('', inplace=True)
        # Verifica se a coluna 'data_nascimento' está presente
        if 'data_nascimento' in df.columns:
            # Aplica formatação da coluna de data de nascimento se necessário
            df['data_nascimento'] = df['data_nascimento'].apply(lambda x: formatar_data(str(x)))
            
            # Preenche valores nulos com 'N/A'
            df = df.fillna('N/A')
            
            # Validar formato do email
            df['email_valido'] = df['email'].apply(lambda x: validar_email(str(x)))
            
            # Remover registros com emails inválidos
            df = df[df['email_valido'].notna()]
            
            # Remover duplicatas baseadas em Data de Nascimento, Email e ID, mantendo o primeiro com mais campos preenchidos
            df['num_campos_preenchidos'] = df.apply(lambda x: x.count(), axis=1)
            df = df.sort_values(by=['num_campos_preenchidos', 'id'], ascending=[False, True])
            df = df.drop_duplicates(subset=['data_nascimento', 'email', 'id'], keep='first')
            
            # Remover colunas auxiliares
            df = df.drop(columns=['num_campos_preenchidos', 'email_valido'])
            
            # Ordenar por ID
            df = df.sort_values(by='id')
            
            return df
        else:
            print("Coluna 'data_nascimento' não encontrada no DataFrame:")
            print(df.head())  # Mostra as primeiras linhas do DataFrame para inspeção
            return None
    except Exception as e:
        print(f"Erro ao limpar dados: {e}")
        return None

def consolidar_dados(csv_df, json_df, excel_df):
    try:
        df_consolidado = pd.concat([csv_df, json_df, excel_df], ignore_index=True)

        # Remover duplicatas após concatenar DFs
        df_consolidado.drop('id', axis=1, inplace=True)
        df_consolidado.drop_duplicates(inplace=True)

        # Substituir células vazias por "Não definido"
        df_consolidado.replace('', 'Não definido', inplace=True)

        return df_consolidado
    except Exception as e:
        print(f"Erro ao consolidar DataFrames: {e}")
        return None

def exportar_excel(df, output_path):
    try:        
        df.to_excel(output_path, index=False)
        print(f"Dados exportados para {output_path} com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar dados para Excel: {e}")

def main():
    df_csv, df_json, df_excel = ler_arquivos(csv_file, json_file, excel_file)
    
    if df_csv is None or df_json is None or df_excel is None:
        print("Erro ao ler os arquivos. Verifique os caminhos e tente novamente.")
        return
    
    df_csv = limpar_dados(df_csv)
    df_json = limpar_dados(df_json)
    df_excel = limpar_dados(df_excel)
    
    if df_csv is None or df_json is None or df_excel is None:
        print("Erro ao limpar os dados. Verifique os dados e tente novamente.")
        return
    
    # Consolidar todos os DataFrames em um único DataFrame
    df_consolidado = consolidar_dados(df_csv, df_json, df_excel)
    
    if df_consolidado is None:
        print("Erro ao consolidar os dados. Verifique os dados e tente novamente.")
        return
    
    # Verificar duplicatas após a consolidação
    num_duplicatas = df_consolidado.duplicated(subset=['data_nascimento', 'email']).sum()
    if num_duplicatas > 0:
        print(f"Foram encontradas {num_duplicatas} duplicatas no DataFrame consolidado.")
        df_consolidado = df_consolidado.drop_duplicates(subset=['data_nascimento', 'email'], keep='first')
        print(f"Duplicatas removidas. Novo tamanho do DataFrame: {len(df_consolidado)}")
    
    # Exportar DataFrame consolidado para o arquivo Excel
    exportar_excel(df_consolidado, 'Python para Dados\\AT\\Mini-Projeto2\\usuarios-consolidados.xlsx')

main()
