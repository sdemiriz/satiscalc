import unittest, json
from lib import globals


class TestGlobalsInstantiation(unittest.TestCase):
    json_file = "tests/test_recipes.json"
    GLOBALS = globals.Globals(json_file=json_file)

    def test_number_recipes_imported(self):
        with open(self.json_file) as j:
            g = json.load(j)
            self.assertEqual(len(g["recipes"]), len(self.GLOBALS.recipes))

    def test_number_items_imported(self):
        with open(self.json_file) as j:
            g = json.load(j)
            self.assertEqual(len(g["items"]), len(self.GLOBALS.items))

    def test_number_machines_imported(self):
        with open(self.json_file) as j:
            g = json.load(j)
            self.assertEqual(len(g["machines"]), len(self.GLOBALS.machines))
