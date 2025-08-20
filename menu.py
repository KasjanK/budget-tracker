import sys
import csv
import dateparser
from transaction import Transaction

# TODO: parse different banks csv exports,
#       add monthly expenses like subscriptions, rent etc,
#       cleanup 

def display_menu():
    print("1. Add a new transaction")
    print("2. Show transactions")
    print("3. Edit transaction")
    print("4. Show monthly report")
    print("q. Exit program")
    
def quit_program():
    sys.exit()

def load_transactions():
    transactions = []
    with open("transactions.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            transactions.append(Transaction.from_csv(row))
    return transactions

def save_transactions(transactions):
    with open("transactions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "category", "amount", "description"])
        for transaction in transactions:
            writer.writerow(transaction.to_csv())

def add_transaction(transactions):
    while True:
            date = input("Enter date of the transaction (YYYY-MM-DD, 'yesterday' or 'next): ")
            date_obj = dateparser.parse(date)
            if date_obj:
                date = date_obj.date()
            break
    category = input("Enter the category of the transaction: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a number:")
            continue
    description = input("Enter description: ")

    transaction = Transaction(date, category, amount, description)
    transactions.append(transaction)
    save_transactions(transactions)

def show_transactions(transactions):
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

def edit_transaction(transactions):
    show_transactions()
    selection = int(input("Choose a transaction to edit: "))
    transaction = transactions[selection - 1]

    transaction.date = input(f"Enter a new date: (Current: {transaction.date}) ")
    transaction.category = input(f"Enter a new category: (Current: {transaction.category})")
    transaction.amount = float(input(f"Enter a new amount: (Current: {transaction.amount})"))
    transaction.description = input(f"Enter a new description: (Current: {transaction.description})")

def show_monthly_report(transactions):
    categories = {}

    for transaction in transactions:
        categories[transaction.category] = categories.get(transaction.category, 0) + transaction.amount

    print("Summary for all transactions: ")
    print("Category        | Amount      |")
    print(f"-"*31)
    for key, value in categories.items():
        print(f"{key:<15} | ${value:<10.2f} |")
