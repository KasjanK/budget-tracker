from datetime import datetime

class Transaction:
    def __init__(self, date, category, amount, description=None):
        if isinstance(date, str):
            self.date = datetime.strptime(date, "%Y-%m-%d").date()
        else:
            self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description
    
    def to_csv(self):
        return [self.date.strftime("%Y-%m-%d"), self.category, self.amount, self.description]
    
    @classmethod
    def from_csv(cls, row):
        date, category, amount, description = row
        return cls(datetime.strptime(date, "%Y-%m-%d").date(), category, float(amount), description)

    def __str__(self):
        return f"{self.date} | {self.category} | {self.amount} | {self.description}"