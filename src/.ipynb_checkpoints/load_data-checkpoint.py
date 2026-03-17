import pandas as pd  
import os       

def load_raw_data(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Data file not found at: {filepath}\n"
            f"Make sure you placed the CSV in data/raw/"
        )

    df = pd.read_csv(filepath, encoding='latin1')


    print(f" Loaded data: {df.shape[0]:,} rows, {df.shape[1]} columns")
 
    return df


def load_processed_data(filepath="data/processed/cleaned_data.csv"):

    return pd.read_csv(filepath)



if __name__ == "__main__":
    df = load_raw_data("data/raw/data.csv")
    print(df.head())
    print(df.dtypes)