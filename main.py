from menu import display_menu, quit_program, add_transaction

def main():
    menu_items = {
        "1": add_transaction,
        "q": quit_program
    }

    while True:
        display_menu()
        selection = input("Choose an option: ")
        menu_items[selection]()

if __name__ == "__main__":
    main()