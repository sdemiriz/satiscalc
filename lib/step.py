import unittest
from lib import tree, item, recipe, globals


class Step:

    def __init__(self, goal: item.Item, globals: globals.Globals):
        self.goal = goal
        self.globals = globals

        self.children = []
        # self.calculate_children()

    def __str__(self) -> str:
        return f"Step: {self.children} -> {self.goal}"

    def calculate_children(self):

        for r in self.globals.recipes:
            if r.has_output(self.goal.name):
                return r
