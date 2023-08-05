import pandas as pd
import matplotlib.pyplot as plt

def exploratory_analysis(file_path):
    # Carregar o arquivo XLSX usando o pandas
    df = pd.read_excel(file_path)

    # Visualizar as primeiras linhas do DataFrame
    print("Primeiras 5 linhas do DataFrame:")
    print(df.head())

    # Informações gerais sobre o DataFrame
    print("\nInformações gerais sobre o DataFrame:")
    print(df.info())

    # Estatísticas descritivas das colunas numéricas
    print("\nEstatísticas descritivas das colunas numéricas:")
    print(df.describe())

    # Verificar valores faltantes por coluna
    print("\nValores faltantes por coluna:")
    print(df.isnull().sum())

    # Contar os valores únicos em cada coluna categórica
    print("\nValores únicos em cada coluna categórica:")
    for col in df.select_dtypes(include='object'):
        print(f"{col}: {df[col].nunique()} unique values")

    # Visualizar a distribuição de algumas colunas numéricas (exemplo: glucose, bloodpressure)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    df['Glucose'].plot(kind='hist', bins=20, title='Distribuição de Glucose')
    plt.subplot(2, 1, 2)
    df['BloodPressure'].plot(kind='hist', bins=20, title='Distribuição de Blood Pressure')
    plt.tight_layout()
    plt.savefig('distribuicao_glucose_bloodpressure.png')
    #plt.show()

    # Verificar correlação entre as colunas numéricas
    print("\nMatriz de Correlação:")
    correlation_matrix = df.corr()
    print(correlation_matrix)

    # Plotar matriz de correlação como heatmap
    plt.figure(figsize=(10, 8))
    plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
    plt.title('Matriz de Correlação')
    plt.colorbar()
    plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=45)
    plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
    plt.savefig('matriz_correlacao.png')
    #plt.show()

if __name__ == "__main__":
    # Substitua "caminho_do_arquivo.xlsx" pelo caminho real do seu arquivo XLSX
    arquivo_xlsx = "diabetes_dataset.xlsx"
    exploratory_analysis(arquivo_xlsx)
