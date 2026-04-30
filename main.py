
import os

from src.etl_pipeline import run_etl
from src.anomaly_detection import detect_anomalies, get_anomaly_summary
from src.visualization import plot_anomalies


def main():
    input_file = "data/raw/sample_network_logs.csv"
    processed_file = "outputs/processed_network_logs.csv"
    anomaly_file = "outputs/flagged_anomalies.csv"
    chart_file = "outputs/anomaly_chart.png"

    os.makedirs("outputs", exist_ok=True)

    df = run_etl(input_file, processed_file)

    df = detect_anomalies(df, column_name="sbytes", threshold=2)

    get_anomaly_summary(df)

    df.to_csv(anomaly_file, index=False)
    print(f"Flagged anomalies saved to {anomaly_file}")

    plot_anomalies(df, column_name="sbytes", output_file=chart_file)

    print("Project completed successfully.")


if __name__ == "__main__":
    main()
