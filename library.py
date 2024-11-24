import csv
from model import Data


def printEntries(entries_list, entries_number=200):
    count = 0
    for entry in entries_list:
        count += 1
        if count >= entries_number:
            break
        print(entry)


def csvRead(path):
    with open(path, "r") as file:
        # reading the CSV file
        csvFile = csv.reader(file)

        # displaying the contents of the CSV file
        entries_list = []
        for lines in csvFile:

            entry = Data(*lines)
            entries_list.append(entry)
    return entries_list
