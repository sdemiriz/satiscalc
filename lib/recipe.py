from lib import item


class Recipe:

    def __init__(
        self,
        name,
        inputs: list[item.Item],
        outputs: list[item.Item],
        time: float,
        machine: str,
        is_alternate: bool,
    ):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.time = time
        self.machine = machine
        self.is_alternate = is_alternate

    def __str__(self):
        return f'Recipe "{self.name}": Converts {self.inputs} to {self.outputs} in machine "{self.machine}" in {self.time} seconds'
