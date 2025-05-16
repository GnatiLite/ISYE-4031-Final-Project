import pandas as pd

def load_and_clean_data(filepath):
    data = pd.read_csv(filepath, skiprows=4)
    data = data.rename(columns={'Country Name': 'Country'})
    data = data.dropna()  # Drop rows with missing values
    return data
