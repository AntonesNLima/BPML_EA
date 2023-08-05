import pandas as pd
from sklearn.linear_model import LinearRegression

def fill_missing_data_with_linear_regression(df, target_column, reference_columns):
    # Replace missing values with 0 for both target and reference columns
    df[reference_columns + [target_column]] = df[reference_columns + [target_column]].fillna(0)

    # Separate the data into features (reference columns) and target (target_column)
    X = df[df[target_column] != 0][reference_columns]
    y = df[df[target_column] != 0][target_column]

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict the missing data using the trained model for rows with missing target_column
    df_missing_data = df[df[target_column] == 0]
    missing_data_predictions = model.predict(df_missing_data[reference_columns])

    # Fill the missing data with the predicted values
    df.loc[df[target_column] == 0, target_column] = missing_data_predictions

    return df

def fill_missing_data_in_file(input_file, output_file):
    # Specify the target columns with missing data
    target_columns_with_missing_data = ["BloodPressure", "SkinThickness", "Insulin", "BMI"]

    # Specify the reference columns for each target column (based on the estimated correlations)
    reference_columns = {
        "BloodPressure": ["Age", "BMI"],
        "SkinThickness": ["Age", "BMI"],
        "Insulin": ["Glucose", "DiabetesPedigreeFunction"],
        "BMI": ["Age", "SkinThickness"]
    }

    # Load the data from the input file into a DataFrame
    df = pd.read_excel(input_file)

    # Fill missing data for each target column using linear regression with the related reference columns
    for target_column in target_columns_with_missing_data:
        df = fill_missing_data_with_linear_regression(df, target_column, reference_columns[target_column])

    # Save the DataFrame with the filled data into the output file
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file names
    input_file_name = "diabetes_dataset.xlsx"
    output_file_name = "diabetes_dataset_linearReg.xlsx"

    # Perform missing data imputation using linear regression and save the result
    fill_missing_data_in_file(input_file_name, output_file_name)
