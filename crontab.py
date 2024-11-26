from datetime import datetime
from libraries.analysis_library import crontabAnalysis
import os

cwd = os.path.dirname(os.path.abspath(__file__))

dataset_path = f"{cwd}/datasets/Customer-Churn-Records.csv"

string_date = datetime.now().strftime("%Y-%m-%d%H%M%S")

with open(f"{cwd}/data/analysis_crontab-{string_date}.txt", "a") as file:
    file.write(f"I am writing from crontab!\n")
    crontab_analysis = crontabAnalysis(dataset_path)
    for key, value in crontab_analysis.items():
        output = f"\nThe Average of number of products bought for {key} points earned is: {value:.2f}\n"
        separator = "-" * len(output)
        file.write(output)
        file.write(separator)
    file.close()