from library import printEntries, csvRead


def main():
    # Generates command line text menu
    print("Welcome to the Bank Churn Data Analysis Menu")
    print("--------------------------------------------")
    print("1. Display Provided Dataset: (Pagination...)")
    print("2. Load CSV Dataset")
    print("3. Analysis")
    print("4. Exit")
    print("--------------------------------------------")

    # Mantains application running
    while True:
        choice = input("Please choose between 1-2: ")
        try:
            number = int(choice)
            if number >= 1 and number < 3:
                if number == 1:
                    # Display Provided Dataset
                    print("Calls function to displays provided datasets.")
                    path = "./Customer-Churn-Records.csv"
                    entry_List = csvRead(path)
                    printEntries(entry_List)
                elif number == 2:
                    # Load CSV Dataset
                    #### we might need to put in a try/catch block here -------
                    print("Load CSV Dataset function")

                    path = input("Please provide a CSV dataset: ")
                    entry_List = csvRead(path)
                    printEntries(entry_List)

                elif number == 3:
                    # Analysis
                    print("Displays Analysis Menu")
                elif number == 4:
                    print("Exiting app...")
                    break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
