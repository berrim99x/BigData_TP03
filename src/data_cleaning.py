import pandas as pd
import os

def load_and_clean_data():

    # Get project root directory
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build correct path to data file
    file_path = os.path.join(base_path, "data", "sales_data.csv")

    # Load data
    data = pd.read_csv(file_path)

    print("Original Data:")
    print(data.head())

    # Remove missing values
    data.dropna(inplace=True)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    # Convert date column
    data['date'] = pd.to_datetime(data['date'])

    print("\nCleaned Data:")
    print(data.head())

    return data