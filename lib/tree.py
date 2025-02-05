from lib import item


class Tree:

    def __init__(self, results: list[item.Item]):
        self.results = results

    def __str__(self):
        return f"Crafting tree that makes {self.results}"

    def __repr__(self):
        return f"Tree(results={self.results})"
