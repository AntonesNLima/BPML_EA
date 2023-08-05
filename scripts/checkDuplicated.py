import pandas as pd

def verificar_dados_duplicados(arquivo):
    # Carregue o arquivo XLSX em um DataFrame
    df = pd.read_excel(arquivo)

    # Verifique se há dados duplicados considerando todas as colunas citadas
    duplicados = df.duplicated(subset=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                                       "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"])

    # Obtenha a quantidade de linhas duplicadas
    quantidade_duplicados = duplicados.sum()

    if quantidade_duplicados > 0:
        print(f"Existem {quantidade_duplicados} linhas duplicadas no arquivo.")
    else:
        print("Não foram encontradas linhas duplicadas.")

if __name__ == "__main__":
    # Especifique o nome do arquivo para verificar os dados duplicados
    arquivo_entrada = "diabetes_dataset_EDV1_normalizado.xlsx"

    # Verifique se há dados duplicados no arquivo
    verificar_dados_duplicados(arquivo_entrada)
