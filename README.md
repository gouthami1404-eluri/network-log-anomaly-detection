# network-log-anomaly-detection
# Network Log Anomaly Detection System

## Overview
This project builds an ETL-based cybersecurity analytics pipeline to detect anomalies in network traffic logs.

## Objective
The goal is to apply data engineering techniques to cybersecurity problems such as suspicious network behavior detection, security analytics, and anomaly detection.

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- CSV-based network log dataset

## Project Workflow
1. Extract network log data from CSV
2. Clean and transform the dataset
3. Apply anomaly detection using Z-score method
4. Flag suspicious records
5. Generate visualization of normal vs anomalous traffic

## Folder Structure

```text
network-log-anomaly-detection/
├── main.py
├── requirements.txt
├── README.md
├── src/
│   ├── etl_pipeline.py
│   ├── anomaly_detection.py
│   └── visualization.py
├── data/
│   └── raw/
│       └── sample_network_logs.csv
└── outputs/
