import unittest
from lib import item


class TestItem(unittest.TestCase):

    name = "Test Name"
    state = "solid"
    rate = 100
    is_raw = False
    test_item = item.Item(name=name, state=state, rate=rate, is_raw=is_raw)

    def test_set_name(self):
        self.assertEqual(self.test_item.name, self.name)

    def test_set_state(self):
        self.assertEqual(self.test_item.state, self.state)

    def test_set_rate(self):
        self.assertEqual(self.test_item.rate, self.rate)

    def test_set_is_raw(self):
        self.assertEqual(self.test_item.is_raw, self.is_raw)


class TestBadState(unittest.TestCase):

    name = "Test Name"
    state = "THIS IS A BAD STATE"
    rate = 100
    is_raw = False

    def test_bad_state(self):
        with self.assertRaises(Exception):
            item.Item(
                name=self.name, state=self.state, rate=self.rate, is_raw=self.is_raw
            )


if __name__ == "__main__":
    unittest.main()
