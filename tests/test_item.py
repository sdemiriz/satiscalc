import unittest
from satiscalc.item import Item


class TestItem(unittest.TestCase):

    name = "Test Name"
    type = "Solid"
    amount = 100
    test_item = Item(name=name, type=type, amount=amount)

    def test_set_name(self):
        unittest.assertEqual(test_item.name, name)

    def test_set_type(self):
        unittest.assertEqual(test_item.type, type)

    def test_set_amount(self):
        unittest.assertEqual(test_item.amount, amount)


if __name__ == "__main__":
    unittest.main()
