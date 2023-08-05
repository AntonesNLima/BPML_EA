import pandas as pd
import matplotlib.pyplot as plt

def generate_boxplot(data, column_name):
    plt.figure(figsize=(8, 6))
    plt.boxplot(data[column_name])
    plt.title(f'Boxplot - {column_name}')
    plt.ylabel(column_name)
    plt.show()

def main():
    # Altere o nome do arquivo XLSX para o caminho correto do seu arquivo.
    file_path = 'diabetes_dataset.xlsx'

    # Leia o arquivo XLSX usando pandas
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
        return
    except Exception as e:
        print(f"Erro: Não foi possível ler o arquivo. Detalhes: {e}")
        return

    # Verifique se as colunas de interesse existem no DataFrame
    columns_of_interest = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    for column_name in columns_of_interest:
        if column_name not in df.columns:
            print(f"A coluna '{column_name}' não existe no arquivo.")
            return

    # Gere o boxplot para cada coluna
    for column_name in columns_of_interest:
        generate_boxplot(df, column_name)

if __name__ == "__main__":
    main()
