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


def printAnalysisEntries(entry_list):
    while True:
        print("\nEnter A: Average credit score by country")
        print("Enter B: Average balance based on age")
        print("Enter C: Average credit score based on tenure")
        print("Enter D: Estimated salary based on gender")
        print("Enter X: Exit")
        user_input = input("Enter Here: ")
        if user_input.upper() == "A":
            geoScoreAvg(entry_list)
        elif user_input.upper() == "B":
            balanceAgeAvg(entry_list)
        elif user_input.upper() == "C":
            tenureScoreAvg(entry_list)
        elif user_input.upper() == "D":
            salaryGenderAvg(entry_list)
        elif user_input.upper() == "X":
            break
        else:
            print("Invalid input!. Please review the options and try again")


def geoScoreAvg(entry_list):
    region = []
    for entry in entry_list:
        if entry.Geography not in region:
            region.append(entry.Geography)
    for country in region:
        creditSum = 0
        countryEntries = 0
        countryScoreAvg = 0
        for entry in entry_list:
            if country == entry.Geography:
                creditSum = creditSum + entry.CreditScore
                countryEntries = countryEntries + 1
        countryScoreAvg = creditSum / countryEntries
        print(
            "The average credit score of "
            + country
            + " is "
            + str(int(countryScoreAvg))
        )


def balanceAgeAvg(entry_list):
    ages = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+"]
    balances = [0, 0, 0, 0, 0, 0, 0, 0]
    entries = [0, 0, 0, 0, 0, 0, 0, 0]
    balanceAverages = [0, 0, 0, 0, 0, 0, 0, 0]
    for entry in entry_list:
        if entry.Age >= 18 and entry.Age <= 29:
            balances[0] = balances[0] + entry.Balance
            entries[0] = entries[0] + 1
        if entry.Age >= 30 and entry.Age <= 39:
            balances[1] = balances[1] + entry.Balance
            entries[1] = entries[1] + 1
        if entry.Age >= 40 and entry.Age <= 49:
            balances[2] = balances[2] + entry.Balance
            entries[2] = entries[2] + 1
        if entry.Age >= 50 and entry.Age <= 59:
            balances[3] = balances[3] + entry.Balance
            entries[3] = entries[3] + 1
        if entry.Age >= 60 and entry.Age <= 69:
            balances[4] = balances[4] + entry.Balance
            entries[4] = entries[4] + 1
        if entry.Age >= 70 and entry.Age <= 79:
            balances[5] = balances[5] + entry.Balance
            entries[5] = entries[5] + 1
        if entry.Age >= 80 and entry.Age <= 89:
            balances[6] = balances[6] + entry.Balance
            entries[6] = entries[6] + 1
        if entry.Age >= 90:
            balances[7] = balances[7] + entry.Balance
            entries[7] = entries[7] + 1
    for i in range(8):
        if entries[i] != 0:
            balanceAverages[i] = balances[i] / entries[i]
        else:
            balanceAverages[i] = 0
    for i in range(8):
        if entries[i] != 0:
            print(
                "The average account balance for ages "
                + ages[i]
                + " is $"
                + ("%.2f" % balanceAverages[i])
            )


def tenureScoreAvg(entry_list):
    tenures = []
    for entry in entry_list:
        if entry.Tenure not in tenures:
            tenures.append(entry.Tenure)
    tenures.sort()
    for tenure in tenures:
        creditSum = 0
        tenureEntries = 0
        tenureScoreAvg = 0
        for entry in entry_list:
            if tenure == entry.Tenure:
                creditSum = creditSum + entry.CreditScore
                tenureEntries = tenureEntries + 1
        tenureScoreAvg = creditSum / tenureEntries
        print(
            "The average credit score of tenure rating "
            + tenure
            + " is "
            + str(int(tenureScoreAvg))
        )


def salaryGenderAvg(entry_list):
    genders = ["Male", "Female"]
    estimatedSalaries = [0, 0]
    entries = [0, 0]
    salaryAverages = [0, 0]
    for entry in entry_list:
        if entry.Gender == genders[0]:
            estimatedSalaries[0] = estimatedSalaries[0] + entry.EstimatedSalary
            entries[0] = entries[0] + 1
        else:
            estimatedSalaries[1] = estimatedSalaries[1] + entry.EstimatedSalary
            entries[1] = entries[1] + 1
    for i in range(2):
        if entries[i] != 0:
            salaryAverages[i] = estimatedSalaries[i] / entries[i]
    for i in range(2):
        if entries[i] != 0:
            print(
                "The overall estimated salary for "
                + genders[i]
                + " is about $"
                + ("%.2f" % salaryAverages[i])
            )
