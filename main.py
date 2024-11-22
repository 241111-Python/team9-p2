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