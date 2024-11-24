import csv
from model import Data


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


def paginate(entries, entry_size, page_number):
    # get the index of the first entry of the page
    start_entry = (page_number - 1) * entry_size
    # get the index of the last entry of the page
    end_entry = start_entry + entry_size

    return entries[start_entry:end_entry]  # we can use list slicing to get each page


def printEntries(entries_list, entry_size=10):
    # sorted each entry based on their credit scores
    sorted_entries = sorted(entries_list, key=lambda x: (x.CreditScore), reverse=True)

    # getting the total number of entries and max number of pages
    total_number_entries = len(sorted_entries)
    max_number_pages = total_number_entries // entry_size

    current_page = 1

    while True:
        current_page_entries = paginate(sorted_entries, entry_size, current_page)
        for entry in current_page_entries:
            print(entry)

        print("__________________________________________________________________")
        print(
            f"_________________________Page {current_page}/{max_number_pages}_____________________________"
        )
        print("Enter N: Next page")
        print("Enter P: Previous page")
        print(f"Enter 1 ~ {max_number_pages}: Go to a specific page")
        print("Enter X: Exit")
        user_input = input("Enter Here: ")
        print("__________________________________________________________________")
        print("__________________________________________________________________")

        if user_input.upper() == "N":
            current_page += 1
            # if user try to exceed the last page, this will make sure the page number stays the same
            if current_page > max_number_pages:
                current_page = max_number_pages
        elif user_input.upper() == "P":
            current_page -= 1
            if current_page < 1:
                current_page = 1
        elif int(user_input) >= 1 and int(user_input) <= max_number_pages:
            current_page = int(user_input)
        elif user_input.upper() == "X":
            break
        else:
            print("Invalid input!. Please review the options and try again")
