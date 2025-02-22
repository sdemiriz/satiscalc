from lib import item, recipe, step


class Tree:

    def __init__(self, results: list[item.Item], recipes: list[recipe.Recipe], items: list[item.Item]):
        self.results = results
        self.recipes = recipes
        self.items = items
        #self.machines = machines

        self.root = []

    def __str__(self) -> str:
        return f"Crafting tree that makes {self.results}"

    def __repr__(self) -> str:
        return f"Tree(results={self.results}, recipes={self.recipes}, items={self.items})"
    
    def save(self, filename) -> None:
        pass

    def load_tree(self, filename):
        pass

    def filter_recipes(self, output: item.Item) -> list[recipe.Recipe]:
        return [r for r in self.recipes if r.has_output(output)]

    def build_tree(self):
        for result in self.results:
            self.root.append(step.Step(goal=result, recipes=self.recipes, items=self.items))

        for child in self.root:
            child.calculate_children()

