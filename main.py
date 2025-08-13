from menu import display_menu, quit_program, add_transaction, show_transactions, edit_transaction, show_monthly_report

def main(): 
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
        menu_items[selection]()

if __name__ == "__main__":
    main()