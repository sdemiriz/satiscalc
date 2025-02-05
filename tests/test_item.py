import unittest
from lib import item


class TestItem(unittest.TestCase):

    name = "Test Name"
    state = "solid"
    amount = 100
    test_item = item.Item(name=name, state=state, amount=amount)

    def test_set_name(self):
        self.assertEqual(self.test_item.name, self.name)

    def test_set_state(self):
        self.assertEqual(self.test_item.state, self.state)

    def test_set_amount(self):
        self.assertEqual(self.test_item.amount, self.amount)


class TestBadState(unittest.TestCase):

    name = "Test Name"
    state = "THIS IS A BAD STATE"
    amount = 100

    def test_bad_state(self):
        with self.assertRaises(Exception):
            item.Item(name=self.name, state=self.state, amount=self.amount)


if __name__ == "__main__":
    unittest.main()
