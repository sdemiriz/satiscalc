import unittest
from lib import item


class TestItemInstantiation(unittest.TestCase):

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


class TestIsRaw(unittest.TestCase):

    name = "Test Name"
    state = "solid"
    rate = 100

    def test_is_raw(self):
        test_item = item.Item(
            name=self.name, state=self.state, rate=self.rate, is_raw=True
        )
        self.assertTrue(test_item.item_is_raw())

    def test_is_not_raw(self):
        test_item = item.Item(
            name=self.name, state=self.state, rate=self.rate, is_raw=False
        )
        self.assertFalse(test_item.item_is_raw())


class TestHasName(unittest.TestCase):

    state = "solid"
    rate = 100
    is_raw = True

    def test_has_name(self):
        test_item = item.Item(
            name="TESTING", state=self.state, rate=self.rate, is_raw=self.is_raw
        )
        self.assertTrue(test_item.item_has_name("TESTING"))

    def test_doesnt_have_name(self):
        test_item = item.Item(
            name="NOT TESTING", state=self.state, rate=self.rate, is_raw=self.is_raw
        )
        self.assertFalse(test_item.item_has_name("TESTING"))


class TestMultiply(unittest.TestCase):

    name = "Test Item"
    state = "solid"
    base_rate = 100
    is_raw = True

    multiplier_int = 10
    multiplier_float = 1.5

    def test_multiply_int(self):
        test_item = item.Item(
            name=self.name, state=self.state, rate=self.base_rate, is_raw=self.is_raw
        )
        test_item.multiply(self.multiplier_int)

        self.assertEqual(test_item.rate, self.base_rate * self.multiplier_int)
        self.assertEqual(test_item.name, test_item.name)
        self.assertEqual(test_item.state, test_item.state)
        self.assertEqual(test_item.is_raw, test_item.is_raw)

    def test_multiply_float(self):
        test_item = item.Item(
            name=self.name, state=self.state, rate=self.base_rate, is_raw=self.is_raw
        )
        test_item.multiply(self.multiplier_float)

        self.assertEqual(test_item.rate, self.base_rate * self.multiplier_float)
        self.assertEqual(test_item.name, test_item.name)
        self.assertEqual(test_item.state, test_item.state)
        self.assertEqual(test_item.is_raw, test_item.is_raw)


if __name__ == "__main__":
    unittest.main()
