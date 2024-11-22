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

def main():
    # Generates command line text menu
    print("Welcome to the Bank Churn Data Analysis Menu")
    print("--------------------------------------------")
    print("1. Load and Display Data")
    print("2. Exit")
    print("--------------------------------------------")

    # Mantains application running
    while True:
        choice = input("Please choose between 1-2: ")
        try:
            number = int(choice)
            if number >= 1 and number < 3:
                if number == 1:
                    print("Calls function to displays data.")
                if number == 2:
                    print("Exiting program...")
                    break
        except ValueError:
            print("Please enter a valid number.")


if __name__  == '__main__':
    main()
