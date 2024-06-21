import pandas as pd

# Caminho dos arquivos
csv_file = 'Python para Dados\AT\Mini-Projeto2\DadosAnalisados\dadosAT.csv'
json_file = 'Python para Dados\AT\Mini-Projeto2\DadosAnalisados\dadosATAntigo.json'
excel_file = 'Python para Dados\AT\Mini-Projeto2\DadosAnalisados\dadosATAntigo.xlsx'

def read_files(csv_path, json_path, excel_path):
    try:
        df_csv = pd.read_csv(csv_path)
        df_json = pd.read_json(json_path)
        df_excel = pd.read_excel(excel_path)
        return df_csv, df_json, df_excel
    except Exception as e:
        print(f"Erro ao ler arquivos: {e}")
        return None, None, None

def clean_data(df):
    try:
        df = df.drop_duplicates()  # Remove duplicatas
        df = df.fillna('N/A')  # Preenche valores nulos
        return df
    except Exception as e:
        print(f"Erro ao limpar dados: {e}")
        return None

def consolidate_data(dfs):
    try:
        consolidated_df = pd.concat(dfs, ignore_index=True)
        return consolidated_df
    except Exception as e:
        print(f"Erro ao consolidar dados: {e}")
        return None

def export_to_excel(df, output_path):
    try:
        df.to_excel(output_path, index=False)
        print(f"Dados exportados para {output_path} com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar dados para Excel: {e}")

def main():
    # Ler os arquivos
    df_csv, df_json, df_excel = read_files(csv_file, json_file, excel_file)
    
    if df_csv is None or df_json is None or df_excel is None:
        print("Erro ao ler os arquivos. Verifique os caminhos e tente novamente.")
        return
    
    # Limpar os dados
    df_csv = clean_data(df_csv)
    df_json = clean_data(df_json)
    df_excel = clean_data(df_excel)
    
    if df_csv is None or df_json is None or df_excel is None:
        print("Erro ao limpar os dados. Verifique os dados e tente novamente.")
        return
    
    # Consolidar os dados
    consolidated_df = consolidate_data([df_csv, df_json, df_excel])
    
    if consolidated_df is None:
        print("Erro ao consolidar os dados. Verifique os dados e tente novamente.")
        return
    
    # Exportar o DataFrame consolidado para um arquivo Excel
    export_to_excel(consolidated_df, 'Python para Dados\AT\Mini-Projeto2\usuarios-consolidados.xlsx')
main()
