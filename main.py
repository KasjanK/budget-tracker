from menu import display_menu, quit_program, add_transaction, show_transactions, edit_transaction, show_monthly_report, load_transactions
import os

def main():
    if not os.path.exists("transactions.csv"):
        with open("transactions.csv", "x") as file:
            file.write("date,category,amount,description")

    transactions = load_transactions()

    menu_items = {
        "1": add_transaction,
        "2": show_transactions,
        "3": edit_transaction,
        "4": show_monthly_report,
        "q": quit_program
    }

    while True:
        display_menu()
        selection = input("Choose an option: ")
        menu_items[selection](transactions)

if __name__ == "__main__":
    main()