import unittest
from lib import tree, item


class TestTree(unittest.TestCase):

    results = [item.Item(name="Test Ingot", state="solid", rate=100)]

    test_tree = tree.Tree(results=results)

    def test_set_results(self):
        self.assertEqual(self.test_tree.results, self.results)


if __name__ == "__main__":
    unittest.main()
