
import numpy as np


def detect_anomalies(df, column_name, threshold=2):
    """
    Detect anomalies using Z-score method.

    If Z-score is greater than threshold,
    the record is marked as suspicious.
    """

    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in dataset.")

    mean_value = df[column_name].mean()
    std_value = df[column_name].std()

    if std_value == 0:
        df["z_score"] = 0
        df["is_anomaly"] = 0
        return df

    df["z_score"] = (df[column_name] - mean_value) / std_value
    df["is_anomaly"] = np.where(abs(df["z_score"]) > threshold, 1, 0)

    print("Anomaly detection completed.")
    return df


def get_anomaly_summary(df):
    """
    Print basic anomaly summary.
    """
    total_records = len(df)
    anomaly_count = df["is_anomaly"].sum()

    print("Total records:", total_records)
    print("Anomalies detected:", anomaly_count)
