class Item:

    __states = ["solid", "liquid", "gas"]

    def __init__(self, name: str, state: str, rate: float, is_raw: bool):
        self.name = name
        self.rate = rate
        self.is_raw = is_raw

        if state not in self.__states:
            raise Exception(f'Supplied state "{state}" is not recognized.')

        self.state = state

    def __str__(self):
        return f"{self.rate} of item {self.name} in state {self.state}"

    def __repr__(self):
        return f"Item(name={self.name}, rate={self.rate}, state={self.state})"
