class Item:

    __states = ["solid", "liquid", "gas"]

    def __init__(self, name: str, state: str, amount: float):
        self.name = name
        self.amount = amount

        if state not in self.__states:
            raise Exception(f'Supplied state "{state}" is not recognized.')

        self.state = state

    def __str__(self):
        return f"{self.amount} of item {self.name} in state {self.state}"

    def __repr__(self):
        return f"Item(name={self.name}, amount={self.amount}, state={self.state})"
