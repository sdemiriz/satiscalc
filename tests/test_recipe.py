import unittest
from lib import item, recipe


class TestRecipe(unittest.TestCase):

    name = "Test Recipe"
    inputs = [item.Item("Test Ore", "solid", 100)]
    outputs = [item.Item("Test Item", "solid", 50)]
    machine = "Constructor"
    is_alternate = False

    test_recipe = recipe.Recipe(
        name=name,
        inputs=inputs,
        outputs=outputs,
        machine=machine,
        is_alternate=is_alternate,
    )

    print(test_recipe)

    def test_set_name(self):
        self.assertEqual(self.test_recipe.name, self.name)

    def test_set_inputs(self):
        self.assertEqual(self.test_recipe.inputs, self.inputs)

    def test_set_outputs(self):
        self.assertEqual(self.test_recipe.outputs, self.outputs)

    def test_set_machine(self):
        self.assertEqual(self.test_recipe.machine, self.machine)

    def test_set_is_alternate(self):
        self.assertEqual(self.test_recipe.is_alternate, self.is_alternate)


if __name__ == "__main__":
    unittest.main()
