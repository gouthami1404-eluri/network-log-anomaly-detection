
import matplotlib.pyplot as plt


def plot_anomalies(df, column_name, output_file):
    """
    Create scatter plot showing normal and anomalous network traffic.
    """
    plt.figure(figsize=(10, 5))

    normal_data = df[df["is_anomaly"] == 0]
    anomaly_data = df[df["is_anomaly"] == 1]

    plt.scatter(normal_data.index, normal_data[column_name], label="Normal")
    plt.scatter(anomaly_data.index, anomaly_data[column_name], label="Anomaly")

    plt.xlabel("Record Index")
    plt.ylabel(column_name)
    plt.title(f"Network Log Anomaly Detection Based on {column_name}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    print(f"Chart saved to {output_file}")
