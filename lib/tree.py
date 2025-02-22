from lib import item, recipe


class Tree:

    def __init__(self, results: list[item.Item], recipes: list[recipe.Recipe], items: list[item.Item]):
        self.results = results
        self.recipes = recipes
        self.items = items
        #self.machines = machines

    def __str__(self) -> str:
        return f"Crafting tree that makes {self.results}"

    def __repr__(self) -> str:
        return f"Tree(results={self.results})"
    
    def save_tree(self) -> None:
        pass

    def load_tree(self):
        pass

