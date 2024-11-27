import csv
from model.customer import CustomerData

columns = {
    "CREDITSCORE": "CreditScore",
    "POINTSEARNED": "Point_Earned",
    "ID": "CustomerId",
    "BALANCE": "Balance",
    "TENURE": "Tenure",
    "GEOGRAPHY": "Geography",
    "AGE": "Age",
    "ESTIMATEDSALARY": "EstimatedSalary",
    "GENDER": "Gender",
}


# Reading and creating objs data from a dataset
def csvRead(path):
    try:
        with open(path, "r") as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            entries_list = []
            # skips header
            next(csvFile)

            for lines in csvFile:
                entry = CustomerData(*lines)
                entries_list.append(entry)
        return entries_list
    except FileNotFoundError:
        print("File Not Found. Please check file's existence or its path again.")


def paginate(entries, entry_size, page_number):
    # get the index of the first entry of the page
    start_entry = (page_number - 1) * entry_size
    # get the index of the last entry of the page
    end_entry = start_entry + entry_size

    return entries[start_entry:end_entry]  # we can use list slicing to get each page


def sort_entries(entries_list, column="ID", order=False):
    column = columns[column]

    return sorted(entries_list, key=lambda x: getattr(x, column), reverse=order)


# Selecting individual entry using a unique identifier (such as CustomerID)
def entry_selection(entries_list, user_input):
    for entry in entries_list:
        if int(user_input) == entry.CustomerId:
            return entry
    print("Entry not found. Please check your ID, and try again.")


def printEntries(entries_list, entry_size=10):
    # sorted each entry based on user preference
    sorted_entries = sort_entries(entries_list)

    # getting the total number of entries and max number of pages
    total_number_entries = len(sorted_entries)
    max_number_pages = total_number_entries // entry_size

    current_page = 1

    header = f"\n{'CustomerId':<10} | {'Surname':<15} | {'Tenure':<6} | {'Credit Score':<15} | {'PointsEarned':<15} | {'Balance':>10}"
    print("_" * len(header))

    while True:
        print("_" * len(header))
        print(
            f"\n{'CustomerId':<10} | {'Surname':<15} | {'Tenure':<6} | {'Credit Score':<12} | {'PointsEarned':<12} | {'Balance':<10}"
        )
        print("_" * len(header))
        current_page_entries = paginate(sorted_entries, entry_size, current_page)
        for entry in current_page_entries:
            print(
                f"\n{entry.CustomerId:<10} | {entry.Surname:<15} | {entry.Tenure:^6} | {entry.CreditScore:^12} | {entry.Point_Earned:^12} | {entry.Balance:<10}"
            )

        print("_" * len(header))
        print(
            f"_______________________________Page {current_page}/{max_number_pages}__________________________________"
        )
        print("Enter N: Next page")
        print("Enter P: Previous page")
        print("Enter G: Getting entry with the <CustomerID>")
        print("Enter S: Sort Data")
        print(f"Enter 1 ~ {max_number_pages}: Go to a specific page")
        print("Enter X: Exit")
        user_input = input("Enter Here: ")
        print("_" * len(header))
        print("_" * len(header))

        if user_input.upper() == "N":
            current_page += 1
            # if user try to exceed the last page, this will make sure the page number stays the same
            if current_page > max_number_pages:
                current_page = max_number_pages

        elif user_input.upper() == "P":
            current_page -= 1
            if current_page < 1:
                current_page = 1

        elif user_input.upper() == "G":

            id_input = input("Please enter CustomerID (15565701 ~ 15815690): ")

            print(
                f"\n{'CustomerId':<10} | {'Surname':<10} | {'Tenure':<6} | {'Credit Score':<12} | {'PointsEarned':<12} | {'Balance':<10}"
            )
            print("_" * len(header))
            entry = entry_selection(entries_list, id_input)
            print(
                f"\n{entry.CustomerId:<10} | {entry.Surname:<10} | {entry.Tenure:^6} | {entry.CreditScore:^12} | {entry.Point_Earned:^12} | {entry.Balance:<10}"
            )
            print()
            print()

        elif user_input.upper() == "S":
            print("Columns available for sorting:")
            print("CreditScore, PointsEarned, Balance, Tenure, Id")

            while True:
                column = input("Enter the column name to sort by: ").strip().upper()
                if column in columns.keys():
                    break

            while True:
                order = (
                    input(
                        "Enter 'asc' for ascending order or 'desc' for descending order: "
                    )
                    .strip()
                    .lower()
                )
                if order == "asc" or order == "desc":
                    break

            sorted_entries = sort_entries(entries_list, column, order == "desc")

        elif user_input.upper() == "X":
            break

        elif int(user_input) >= 1 and int(user_input) <= max_number_pages:
            current_page = int(user_input)

        else:
            print("Invalid input!. Please review the options and try again")
