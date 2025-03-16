from lib import item, recipe, step, globals


class Tree:

    def __init__(self, results: list[item.Item], globals: globals.Globals):
        self.results = results
        self.globals = globals
        # self.machines = machines

        self.steps = []
        for r in self.results:
            self.steps.append(step.Step(goal=r, globals=self.globals))

    def __str__(self) -> str:
        return f"Crafting tree that makes {self.results}"

    def __repr__(self) -> str:
        return f"Tree(results={self.results})"

    def save(self, filename) -> None:
        pass

    def load_tree(self, filename):
        pass

    def filter_recipes(self, output: item.Item) -> list[recipe.Recipe]:
        return [r for r in self.globals.recipes if r.has_output(output)]

    def build_tree(self):
        for step in self.steps:
            step.calculate_children()
