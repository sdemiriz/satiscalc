class Item:

    __states = ["solid", "liquid", "gas"]

    def __init__(self, name: str, state: str, rate: float, is_raw: bool):
        """
        Instantiate item
        """
        self.name = name
        self.rate = rate
        self.is_raw = is_raw

        if state not in self.__states:
            raise Exception(f'Supplied state "{state}" is not recognized.')

        self.state = state

    def __str__(self) -> str:
        """
        Return string representation of item
        """
        return f"{self.rate} of item {self.name} in state {self.state}"

    def __repr__(self) -> str:
        """
        Return string representation of item call
        """
        return f"Item(name={self.name}, rate={self.rate}, state={self.state})"

    def multiply(self, other) -> None:
        self.rate *= other

    def item_is_raw(self) -> bool:
        """
        Return whether the item is a raw input (resource)
        """
        return self.is_raw

    def item_has_name(self, name_query) -> bool:
        """
        Return whether the item has the queried name (resource)
        """
        return self.name == name_query
