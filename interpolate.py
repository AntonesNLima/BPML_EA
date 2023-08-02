import pandas as pd

def tratar_dados_faltantes_com_interpolar(df, colunas):
    # Interpole os dados faltantes nas colunas especificadas
    df[colunas] = df[colunas].interpolate(method='linear', axis=0)

    return df

def tratar_dados_faltantes_arquivo(entrada, colunas, saida):
    # Carregue o arquivo XLSX em um DataFrame
    df = pd.read_excel(entrada)

    # Realize o tratamento de dados faltantes com interpolação nas colunas especificadas
    df = tratar_dados_faltantes_com_interpolar(df, colunas)

    # Salve os novos dados tratados em um novo arquivo XLSX
    df.to_excel(saida, index=False)

if __name__ == "__main__":
    # Especifique o nome do arquivo de entrada e saída
    arquivo_entrada = "diabetes_dataset.xlsx"
    arquivo_saida = "diabetes_dataset_interpolate.xlsx"

    # Especifique as colunas com dados faltantes a serem tratadas
    colunas_com_dados_faltantes = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    # Realize o tratamento de dados faltantes com interpolação e salve o novo arquivo
    tratar_dados_faltantes_arquivo(arquivo_entrada, colunas_com_dados_faltantes, arquivo_saida)
