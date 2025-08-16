import sys
from transaction import Transaction

# TODO: import/export to/from csv file,
#       fix proper dating system,
#       check for right inputs, string for date and float for amount etc,
#       add monthly expenses like subscriptions, rent etc,
#       sort monthly report from highest to lowest

transactions = [
    Transaction(date="2025-07-14", category="Food", amount=15.99, description="Grocery shopping"),
    Transaction(date="2025-07-15", category="Rent", amount=8004.2, description="Monthly rent"),
    Transaction(date="2025-07-16", category="Transport", amount=3.50, description="Bus fare"),
    Transaction(date="2025-07-14", category="Food", amount=15.99, description="Grocery shopping"),
]

def display_menu():
    print("1. Add a new transaction")
    print("2. Show transactions")
    print("3. Edit transaction")
    print("4. Show monthly report")
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
    total = 0
    print("Your Transactions:")
    print("#  Date       | Category        | Amount      | Description")
    print(f"-"*65)
    for index, t in enumerate(transactions, start=1):
        print(f"{index}. {t.date} | {t.category:<15} | ${t.amount:<10.2f} | {t.description}")
    for t in transactions:
        total += t.amount
    print(f"-"*65)
    print(f"Total amount spent: {total:.2f}")
    print(f"-"*65)


def edit_transaction():
    show_transactions()
    selection = int(input("Choose a transaction to edit: "))
    transaction = transactions[selection - 1]

    transaction.date = input(f"Enter a new date: (Current: {transaction.date}) ")
    transaction.category = input(f"Enter a new category: (Current: {transaction.category})")
    transaction.amount = float(input(f"Enter a new amount: (Current: {transaction.amount})"))
    transaction.description = input(f"Enter a new description: (Current: {transaction.description})")

def show_monthly_report():
    categories = {}

    for transaction in transactions:
        categories[transaction.category] = categories.get(transaction.category, 0) + transaction.amount

    print("Summary for all transactions: ")
    print("Category        | Amount      |")
    print(f"-"*31)
    for key, value in categories.items():
        print(f"{key:<15} | ${value:<10.2f} |")
