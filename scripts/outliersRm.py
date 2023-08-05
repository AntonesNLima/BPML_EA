import pandas as pd

def trata_dados_discrepantes(df, coluna):
    # Calcule os limites inferior e superior para tratar os dados discrepantes
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    # Substitua os valores discrepantes pelos limites e conte as modificações
    count_modificados = 0
    for idx, valor in enumerate(df[coluna]):
        if valor < limite_inferior:
            df.at[idx, coluna] = limite_inferior
            count_modificados += 1
        elif valor > limite_superior:
            df.at[idx, coluna] = limite_superior
            count_modificados += 1

    return df, count_modificados

def tratar_dados_discrepantes_arquivo(entrada, colunas, saida):
    # Carregue o arquivo XLSX em um DataFrame
    df = pd.read_excel(entrada)

    total_modificados = 0
    # Realize o tratamento de dados discrepantes por coluna
    for coluna in colunas:
        df, count_modificados = trata_dados_discrepantes(df, coluna)
        total_modificados += count_modificados
        print(f"Coluna '{coluna}': {count_modificados} valores modificados.")

    # Salve os novos dados em um novo arquivo XLSX
    df.to_excel(saida, index=False)

    print(f"Total de valores modificados: {total_modificados}")

if __name__ == "__main__":
    # Especifique o nome do arquivo de entrada e saída
    arquivo_entrada = "diabetes_dataset_EDV1_normalizado.xlsx"
    arquivo_saida = "diabetes_dataset_EDV1_normalizado_woOutliers.xlsx"

    # Especifique as colunas a serem tratadas
    colunas_para_tratar = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    ]

    # Realize o tratamento de dados discrepantes e salve o novo arquivo
    tratar_dados_discrepantes_arquivo(arquivo_entrada, colunas_para_tratar, arquivo_saida)
