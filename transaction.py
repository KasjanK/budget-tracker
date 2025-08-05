class Transaction:
    def __init__(self, date, category, amount, description=None):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"