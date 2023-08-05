import pandas as pd

# Load the data from the XLSX file into a DataFrame
df = pd.read_excel("diabetes_dataset_normalizado.xlsx")

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Define the threshold values for strong, moderate, and weak correlation
strong_correlation_threshold = 0.7
moderate_correlation_threshold = 0.5

# Create a dictionary to store the correlation classification
correlation_classification = {}

# Iterate through the correlation matrix to classify correlations
for col1 in correlation_matrix.columns:
    for col2 in correlation_matrix.columns:
        if col1 != col2:
            correlation_value = correlation_matrix.loc[col1, col2]
            if correlation_value >= strong_correlation_threshold:
                correlation_classification[(col1, col2)] = "S"
            elif correlation_value <= -strong_correlation_threshold:
                correlation_classification[(col1, col2)] = "SN"
            elif abs(correlation_value) >= moderate_correlation_threshold:
                correlation_classification[(col1, col2)] = "M"
            else:
                correlation_classification[(col1, col2)] = "W"

# Display the correlation classification matrix
columns = correlation_matrix.columns
correlation_df = pd.DataFrame(index=columns, columns=columns)

for col1 in columns:
    for col2 in columns:
        if col1 != col2:
            correlation_df.loc[col1, col2] = correlation_classification.get((col1, col2), "")

print(correlation_df)
