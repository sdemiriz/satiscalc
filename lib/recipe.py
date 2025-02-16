from lib import item


class Recipe:

    def __init__(
        self,
        name,
        inputs: list[item.Item],
        outputs: list[item.Item],
        machine: str,
        is_alternate: bool,
    ):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.machine = machine
        self.is_alternate = is_alternate

    def __str__(self) -> str:
        return f'Recipe "{self.name}": Converts {self.inputs} to {self.outputs} in machine "{self.machine}"'

    def __repr__(self) -> str:
        return f'Recipe "{self.name}": Converts {self.inputs} to {self.outputs} in machine "{self.machine}"'

    def multiply(self, other: float) -> None:

        assert other > 0, f"Multiplier cannot be zero or negative, multiplier: {other}"

        for i in self.inputs:
            i.multiply(other)

        for o in self.outputs:
            o.multiply(other)

    def recipe_is_alt(self) -> bool:
        return self.is_alternate

    def has_input(self, query_name: str) -> bool:
        return query_name in [i.name for i in self.inputs]

    def has_output(self, query_name: str) -> bool:
        return query_name in [i.name for i in self.outputs]
