class Item:
    def __init__(self, name: str, type: str, amount: float):
        self.name = name
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.amount} of item {self.name} of type {self.type}"
