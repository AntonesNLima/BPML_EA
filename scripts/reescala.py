import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data_using_rescaling(df, columns_to_normalize):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Fit and transform the specified columns with MinMaxScaler
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

    return df

def normalize_data_in_file(input_file, output_file, columns_to_normalize):
    # Load the data from the input file into a DataFrame
    df = pd.read_excel(input_file)

    # Normalize the specified columns using reescaling
    df = normalize_data_using_rescaling(df, columns_to_normalize)

    # Save the DataFrame with the normalized data into the output file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file names
    input_file_name = "diabetes_dataset_interpolate.xlsx"
    output_file_name = "diabetes_dataset_interpolate_reescala.xlsx"

    # Specify the columns to be normalized using reescaling
    columns_to_normalize = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

    # Perform data normalization using reescaling and save the result
    normalize_data_in_file(input_file_name, output_file_name, columns_to_normalize)
