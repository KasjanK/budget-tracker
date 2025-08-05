from transaction import Transaction

def main():
    t = Transaction("2025-08-05", "Food", "375.25", "Groceries")
    t.date = input("Enter date of the transaction: ")
    t.category = input("Enter the category of the transaction: ")
    t.amount = input("Enter amount: ")
    t.description = input("Enter description: ")
    print(t)

if __name__ == "__main__":
    main()