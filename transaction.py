class Transaction:
    def __init__(self, date, category, amount, description=None):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description
    
    def to_csv(self):
        return [self.date, self.category, self.amount, self.description]
    
    @classmethod
    def from_csv(cls, row):
        date, category, amount, description = row
        return cls(date, category, float(amount), description)

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"