import unittest
from lib import item, recipe


class TestRecipeInstantiate(unittest.TestCase):

    name = "Test Recipe"
    inputs = [item.Item("Test Ore", "solid", 100, is_raw=False)]
    outputs = [item.Item("Test Item", "solid", 50, is_raw=False)]
    machine = "Constructor"
    is_alternate = False

    test_recipe = recipe.Recipe(
        name=name,
        inputs=inputs,
        outputs=outputs,
        machine=machine,
        is_alternate=is_alternate,
    )

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


class TestRecipeIsAlternate(unittest.TestCase):

    name = "Test Recipe"
    inputs = [item.Item("Test Ore", "solid", 100, is_raw=False)]
    outputs = [item.Item("Test Item", "solid", 50, is_raw=False)]
    machine = "Constructor"

    def test_is_alternate(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=self.inputs,
            outputs=self.outputs,
            machine=self.machine,
            is_alternate=True,
        )
        self.assertTrue(test_recipe.recipe_is_alt())

    def test_is_not_alternate(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=self.inputs,
            outputs=self.outputs,
            machine=self.machine,
            is_alternate=False,
        )
        self.assertFalse(test_recipe.recipe_is_alt())


class TestRecipeHasInput(unittest.TestCase):

    name = "Test Recipe"
    outputs = [item.Item("Test Item", "solid", 50, is_raw=False)]
    machine = "Constructor"

    test_input_name = "Test Ore"

    def test_has_input(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item(self.test_input_name, "solid", 100, is_raw=False)],
            outputs=self.outputs,
            machine=self.machine,
            is_alternate=False,
        )
        self.assertTrue(test_recipe.has_input(self.test_input_name))

    def test_doesnt_have_input(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item("Not Test Ore", "solid", 100, is_raw=False)],
            outputs=self.outputs,
            machine=self.machine,
            is_alternate=True,
        )
        self.assertFalse(test_recipe.has_input(self.test_input_name))


class TestRecipeHasOutput(unittest.TestCase):

    name = "Test Recipe"
    inputs = [item.Item("Test Ore", "solid", 50, is_raw=False)]
    machine = "Constructor"

    test_output_name = "Test Item"

    def test_has_input(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=self.inputs,
            outputs=[item.Item(self.test_output_name, "solid", 100, is_raw=False)],
            machine=self.machine,
            is_alternate=False,
        )
        self.assertTrue(test_recipe.has_output(self.test_output_name))

    def test_doesnt_have_input(self):
        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=self.inputs,
            outputs=[item.Item("Not Test Item", "solid", 100, is_raw=False)],
            machine=self.machine,
            is_alternate=True,
        )
        self.assertFalse(test_recipe.has_output(self.test_output_name))


class TestRecipeMultiply(unittest.TestCase):

    base_rate_in = 50
    base_rate_out = 100

    name = "Test Recipe"
    machine = "Constructor"

    def test_multiply_int(self):

        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item("Test Ore", "solid", self.base_rate_in, is_raw=True)],
            outputs=[
                item.Item("Test Ingot", "solid", self.base_rate_out, is_raw=False)
            ],
            machine=self.machine,
            is_alternate=False,
        )

        multiplier_int = 10
        test_recipe.multiply(multiplier_int)

        self.assertEqual(
            [i.rate for i in test_recipe.inputs],
            [self.base_rate_in * multiplier_int for i in test_recipe.inputs],
        )
        self.assertEqual(
            [o.rate for o in test_recipe.outputs],
            [self.base_rate_out * multiplier_int for o in test_recipe.outputs],
        )
        self.assertEqual(test_recipe.name, self.name)
        self.assertEqual(test_recipe.machine, self.machine)

    def test_multiply_float(self):

        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item("Test Ore", "solid", self.base_rate_in, is_raw=True)],
            outputs=[
                item.Item("Test Ingot", "solid", self.base_rate_out, is_raw=False)
            ],
            machine=self.machine,
            is_alternate=False,
        )

        multiplier_float = 2.5
        test_recipe.multiply(multiplier_float)

        self.assertEqual(
            [i.rate for i in test_recipe.inputs],
            [self.base_rate_in * multiplier_float for i in test_recipe.inputs],
        )
        self.assertEqual(
            [o.rate for o in test_recipe.outputs],
            [self.base_rate_out * multiplier_float for o in test_recipe.outputs],
        )
        self.assertEqual(test_recipe.name, self.name)
        self.assertEqual(test_recipe.machine, self.machine)

    def test_multiply_negative(self):

        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item("Test Ore", "solid", self.base_rate_in, is_raw=True)],
            outputs=[
                item.Item("Test Ingot", "solid", self.base_rate_out, is_raw=False)
            ],
            machine=self.machine,
            is_alternate=False,
        )

        multiplier_negative = -2

        with self.assertRaises(Exception):
            test_recipe.multiply(multiplier_negative)

    def test_multiply_zero(self):

        test_recipe = recipe.Recipe(
            name=self.name,
            inputs=[item.Item("Test Ore", "solid", self.base_rate_in, is_raw=True)],
            outputs=[
                item.Item("Test Ingot", "solid", self.base_rate_out, is_raw=False)
            ],
            machine=self.machine,
            is_alternate=False,
        )

        multiplier_zero = 0

        with self.assertRaises(Exception):
            test_recipe.multiply(multiplier_zero)


if __name__ == "__main__":
    unittest.main()
