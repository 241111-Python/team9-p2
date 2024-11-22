import csv
from model import Data
import library

# opening the CSV file
path = "./Customer-Churn-Records.csv"
# path = input()

with open(path, "r") as file:
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    count = 0
    entries_list = []
    for lines in csvFile:
        # BREAK. taking only 200 for now
        count += 1
        if count >= 200:
            break

        entry = Data(*lines)
        entries_list.append(entry)

    for entry in entries_list:
        print(entry)
