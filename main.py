from library import printEntries, csvRead, printAnalysisEntries
import argparse


def main():
    # Mantains application running
    while True:
        # Generates command line text menu
        print("__________________________________________________________________")
        print("\nWelcome to the Bank Churn Data Analysis Menu")
        print("__________________________________________________________________")
        print("\n1. Display Provided Dataset: (Pagination...)")
        print("2. Load CSV Dataset to Display or Analyze")
        print("3. Analysis")
        print("4. Exit")
        print("__________________________________________________________________")

        choice = input("\nEnter Here: ")

        try:
            number = int(choice)
            if number >= 1 and number <= 4:
                if number == 1:
                    # Display Provided Dataset
                    path = "./datasets/Customer-Churn-Records.csv"
                    entry_List = csvRead(path)
                    printEntries(entry_List)
                elif number == 2:
                    # Load CSV Dataset
                    print(
                        "To load a CSV Dataset, use the following command in your terminal: "
                    )
                    print(
                        "\npy main.py --load-dataset ./datasets/your-dataset-name.csv\n"
                    )
                    print("Exiting app...")
                    break

                elif number == 3:
                    # Analysis
                    path = "./datasets/Customer-Churn-Records.csv"
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
        description="Argpaser for project 2: load_dataset"
    )

    my_parser.add_argument(
        "--load-dataset",
        type=str,
        choices=["display", "analyze"],
        help="Load dataset from ./dataset directory either to display or analyze it. Please ensures it exists there.",
    )

    user_args = my_parser.parse_args()
    if user_args.load_dataset:
        if user_args.load_dataset.split(" ")[1] == "display":
            # getting the path from the first part of argument
            path = user_args.load_dataset.split(" ")[0]

            print(f"Loading dataset from {path}")
            print("Displaying the dataset: (Pagination)")
            entry_List = csvRead(path)
            # Display the dataset in pagination
            printEntries(entry_List)
        elif user_args.load_dataset.split(" ")[1] == "analyze":
            # getting the path from the first part of argument
            path = user_args.load_dataset.split(" ")[0]

            print(f"Loading dataset from {path}")
            entry_List = csvRead(path)
            # Starting the analysis with choosing options
            printAnalysisEntries(entry_List)
    else:
        main()
