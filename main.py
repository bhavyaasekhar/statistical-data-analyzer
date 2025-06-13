from analyzer.io import load_csv
from analyzer.statistics import (
    calculate_mean,
    calculate_median,
    calculate_mode,
    calculate_variance,
    calculate_std_deviation,
    calculate_correlation_matrix,
    detect_outliers_z_score,
    detect_outliers_iqr
)


def main():
    data = load_csv("data/sample.csv")

    print("📊 Data:\n", data)

    print("\n📈 Mean:\n", calculate_mean(data))
    print("\n📉 Median:\n", calculate_median(data))
    print("\n🔁 Mode:\n", calculate_mode(data))
    print("\n📊 Variance:\n", calculate_variance(data))
    print("\n📏 Standard Deviation:\n", calculate_std_deviation(data))
    print("\n🔗 Correlation Matrix:\n", calculate_correlation_matrix(data))
    print("\n🚨 Outliers (Z-Score):\n", detect_outliers_z_score(data))
    print("\n📦 Outliers (IQR):\n", detect_outliers_iqr(data))


if __name__ == "__main__":
    main()
