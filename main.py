from library import printEntries, csvRead


def main():
    # Mantains application running
    while True:
        # Generates command line text menu
        print("__________________________________________________________________")
        print("\nWelcome to the Bank Churn Data Analysis Menu")
        print("__________________________________________________________________")
        print("\n1. Display Provided Dataset: (Pagination...)")
        print("2. Load CSV Dataset")
        print("3. Analysis")
        print("4. Exit")
        print("__________________________________________________________________")

        choice = input("\nPlease choose between 1-4: ")

        try:
            number = int(choice)
            if number >= 1 and number <= 4:
                if number == 1:
                    # Display Provided Dataset
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
