import sys
from transaction import Transaction

def display_menu():
    print("1. Add a new transaction")
    print("q. Exit program")
    
def quit_program():
    sys.exit()

def add_transaction():
    date = input("Enter date of the transaction: ")
    category = input("Enter the category of the transaction: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")
    transaction = Transaction(date, category, amount, description)
    print(transaction)