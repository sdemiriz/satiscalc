import unittest
import json
from lib import tree, item, recipe


class TestTreeInitialization(unittest.TestCase):

    results = [item.Item(name="Test Ingot", state="solid", rate=100, is_raw=False)]

    test_tree = tree.Tree(results=results, recipes=None, items=None)

    def test_set_results(self):
        self.assertEqual(self.test_tree.results, self.results)

class TestTreeBuildTree(unittest.TestCase):

    with open('tests/test_recipes.json') as recipe_file:
        recipe_json = json.load(recipe_file)
        all_recipes = [recipe.Recipe(name=r["name"], 
                                     inputs=[item.Item(name=i["name"], state="solid", rate=i["rate"], is_raw=False) for i in r["inputs"]], 
                                     outputs=[item.Item(name=i["name"], state="solid", rate=i["rate"], is_raw=False) for i in r["outputs"]], 
                                     machine=r["machine"],
                                     is_alternate=r["is_alternate"]) for r in recipe_json["recipes"]]

    result = [item.Item(name="Test Plate", state="solid", rate=100, is_raw=True)]
    test_tree = tree.Tree(results=result, recipes=all_recipes, items=None)

    test_tree.build_tree()


if __name__ == "__main__":
    unittest.main()
