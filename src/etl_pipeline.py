
import pandas as pd


def load_data(file_path):
    """
    Load network log data from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        raise


def clean_data(df):
    """
    Clean network log data by removing duplicates,
    handling missing values, and converting timestamp.
    """
    df = df.drop_duplicates()
    df = df.fillna(0)

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    print("Data cleaned successfully.")
    return df


def save_processed_data(df, output_path):
    """
    Save cleaned data to CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


def run_etl(input_path, output_path):
    """
    Full ETL process.
    """
    df = load_data(input_path)
    df = clean_data(df)
    save_processed_data(df, output_path)
    return df
