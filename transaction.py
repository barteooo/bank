from datetime import datetime


class Transaction:
    def __init__(self, amount, type, description, source_account=None, destination_account=None):
        self.amount = amount
        self.type = type
        self.description = description
        self.timestamp = datetime.now()
        self.source_account = source_account
        self.destination_account = destination_account

    def __repr__(self):
        if self.type == "Przelew wchodzący" or self.type == "Przelew wychodzący":
            return f"{self.timestamp} - {self.type} - {self.amount} - {self.description} - {self.source_account} - {self.destination_account}"
        else:
            return f"{self.timestamp} - {self.type} - {self.amount} - {self.description}"


