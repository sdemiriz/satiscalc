import unittest
from lib import tree, item, recipe

class Step:

    def __init__(self, goal: item.Item, recipes: list[recipe.Recipe], items: list[item.Item]):
        self.goal = goal
        self.recipes = recipes
        self.items = items

        self.children = []

    def __str__(self) -> str:
        return f"Step to make {self.goal} from {self.children}"

    def calculate_children(self):
        # print(f"Can use the following recipes:\n{self.recipes}")

        out = [r for r in self.recipes if r.has_output(self.goal)]
        self.children.append(Step(goal=None, recipes=out, items=None))
        
        self.calculate_children()