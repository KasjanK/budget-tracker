# 💰 Personal Budget Tracker

A Python command-line application to track personal expenses.  
You can add, view, edit, and delete transactions, generate reports, and save your data to a file so it persists across runs.

---

## Features

- Add new expenses
- View all expenses in a clean list
- Edit or delete existing expenses
- Generate a monthly report (totals per category, total spending)
- (Ongoing) Save all transactions to a CSV file
- (Ongoing) Automatically load transactions on startup
- (Planned) Category budgets with warnings
- (Planned) Data visualization with charts

---

## Tech Stack

- **Language:** Python 3.10+
- **Storage:** CSV file (`transactions.csv`)

---

## Getting Started

### 1. Clone the Repository
```
git clone https://github.com/yourusername/budget-tracker.git
cd budget-tracker
```

### 2. Run the program
```
python main.py
```

The program will automatically create a transactions.csv file if it doesn’t exist, and load your transactions if it does.

## Example Usage
```
1. Add Expense
2. View Expenses
3. Edit/Delete Expense
4. Monthly Report
q. Quit
-------------------------------
Choose an option: 1

Enter date (YYYY-MM-DD): 2025-07-14
Enter category: Food
Enter amount: 15.99
Enter description: Grocery shopping
```

## Roadmap

- [x] Add, view, edit, and delete expenses  
- [x] Generate monthly reports  
- [ ] Save and load transactions from CSV  
- [ ] Implement recurring expenses  
- [ ] Improve CLI design  
- [ ] Optional: Build a simple GUI (Tkinter or Streamlit)  
- [ ] Optional:  visualization (pie charts, bar graphs)  
