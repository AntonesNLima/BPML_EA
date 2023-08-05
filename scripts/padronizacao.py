import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalizar_por_padronizacao(df, colunas):
    # Inicialize o scaler
    scaler = StandardScaler()

    # Aplique a padronização nas colunas especificadas
    df[colunas] = scaler.fit_transform(df[colunas])
    return df

def normalizar_arquivo_por_padronizacao(entrada, colunas, saida):
    # Carregue o arquivo XLSX em um DataFrame
    df = pd.read_excel(entrada)

    # Realize a normalização por padronização nas colunas especificadas
    df = normalizar_por_padronizacao(df, colunas)

    # Salve os novos dados normalizados em um novo arquivo XLSX
    df.to_excel(saida, index=False)

if __name__ == "__main__":
    # Especifique o nome do arquivo de entrada e saída
    arquivo_entrada = "diabetes_dataset_linearReg.xlsx"
    arquivo_saida = "diabetes_dataset_linearReg_normalizado.xlsx"

    # Especifique as colunas a serem normalizadas
    colunas_para_normalizar = [
        "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
    ]

    # Realize a normalização por padronização e salve o novo arquivo
    normalizar_arquivo_por_padronizacao(arquivo_entrada, colunas_para_normalizar, arquivo_saida)
