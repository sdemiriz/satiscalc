import unittest
import json
from lib import tree, item, recipe, globals


class TestTreeInitialization(unittest.TestCase):

    results = [item.Item(name="Test Ingot", state="solid", rate=100, is_raw=False)]
    test_tree = tree.Tree(
        results=results, globals=globals.Globals("tests/test_recipes.json")
    )

    def test_set_results(self):
        self.assertEqual(self.test_tree.results, self.results)


class TestTreeBuildTree(unittest.TestCase):

    results = [item.Item(name="Test Plate", state="solid", rate=100, is_raw=False)]
    test_tree = tree.Tree(
        results=results, globals=globals.Globals("tests/test_recipes.json")
    )

    test_tree.build_tree()


if __name__ == "__main__":
    unittest.main()
