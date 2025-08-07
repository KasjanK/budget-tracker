import sys
from transaction import Transaction

transactions = [
    Transaction(date="2025-07-14", category="Food", amount=15.99, description="Grocery shopping"),
    Transaction(date="2025-07-15", category="Rent", amount=8004.2, description="Monthly rent"),
    Transaction(date="2025-07-16", category="Trans", amount=3.50, description="Bus fare")
]

def display_menu():
    print("1. Add a new transaction")
    print("2. Show transactions")
    print("3. Edit transaction")
    print("q. Exit program")
    
def quit_program():
    sys.exit()

def add_transaction():
    date = input("Enter date of the transaction: ")
    category = input("Enter the category of the transaction: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    transactions.append(Transaction(date, category, amount, description))

def show_transactions():
    print("Your Transactions:")
    print("#  Date       | Category        | Amount      | Description")
    print(f"-"*65)
    for index, t in enumerate(transactions, start=1):
        print(f"{index}. {t.date} | {t.category:<15} | ${t.amount:<10.2f} | {t.description}")
    print(f"-"*65)

def edit_transaction():
    show_transactions()
    selection = int(input("Choose a transaction to edit: "))
    transaction = transactions[selection - 1]

    transaction.date = input(f"Enter a new date: (Current: {transaction.date}) ")
    transaction.category = input(f"Enter a new category: (Current: {transaction.category})")
    transaction.amount = float(input(f"Enter a new amount: (Current: {transaction.amount})"))
    transaction.description = input(f"Enter a new description: (Current: {transaction.description})")
