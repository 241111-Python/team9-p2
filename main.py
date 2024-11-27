from libraries.library import printEntries, csvRead
from libraries.analysis_library import printAnalysisEntries
import argparse


# Main function, where application starts and ends
def main():
    path = "./datasets/Customer-Churn-Records.csv"
    # Mantains application running
    while True:
        # Generates command line text menu
        print("__________________________________________________________________")
        print("\nWelcome to the Bank Churn Data Analysis Menu")
        print("__________________________________________________________________")
        print("\n1. Display Provided Dataset: (Pagination...)")
        print("2. Load CSV Dataset to Display or Analyze")
        print("3. Analysis (On default dataset)")
        print("4. Exit")
        print("__________________________________________________________________")

        choice = input("\nEnter Here: ")

        try:
            number = int(choice)
            if number >= 1 and number <= 4:
                if number == 1:
                    # Display Provided Dataset
                    entry_List = csvRead(path)
                    printEntries(entry_List)
                elif number == 2:
                    # Load CSV Dataset instructions
                    print(
                        "To load a CSV Dataset, use the following command in your terminal: "
                    )
                    print(
                        "\npy main.py --load-dataset ./datasets/dataset-name.csv --display-analyze (either display or analyze)\n"
                    )
                    print("Exiting app...")
                    break

                elif number == 3:
                    # Analysis process
                    entry_List = csvRead(path)
                    printAnalysisEntries(entry_List)
                elif number == 4:
                    print("Exiting app...")
                    break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input. Please enter a valid number (1 ~ 4).")


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(
        description="Argpaser for project 2: load_dataset for displaying or analyzing"
    )

    # first argument is for loading dataset
    my_parser.add_argument(
        "--load-dataset",
        type=str,
        help="Load dataset from ./dataset directory either to display or analyze it. Please ensures it exists there.",
    )

    # second argument is for choosing either to display or analyze the loaded dataset
    my_parser.add_argument(
        "--display-analyze",
        type=str,
        choices=["display", "analyze"],
        help="Use the dataset to display or analyze it.",
    )

    # get and store user arguments
    user_args = my_parser.parse_args()

    if user_args.load_dataset and user_args.display_analyze:
        if user_args.display_analyze == "display":
            # getting the path from the first part of argument
            path = user_args.load_dataset

            print(f"Loading dataset from {path}")
            print("Displaying the dataset: (Pagination)")
            entry_List = csvRead(path)
            # Display the dataset in pagination
            printEntries(entry_List)
        elif user_args.display_analyze == "analyze":
            # getting the path from the first part of argument
            path = user_args.load_dataset

            print(f"Loading dataset from {path}")
            entry_List = csvRead(path)
            # Starting the analysis with choosing options
            printAnalysisEntries(entry_List)
    else:
        # if there is nothing in the argument(s), the app will use the default dataset.
        main()
