import unittest
from lib import machine


class TestMachine(unittest.TestCase):

    name = "Test Machine"
    power = 100
    num_belt_inputs = 1
    num_pipe_inputs = 2
    num_belt_outputs = 3
    num_pipe_outputs = 4

    test_machine = machine.Machine(
        name=name,
        power=power,
        num_belt_inputs=num_belt_inputs,
        num_pipe_inputs=num_pipe_inputs,
        num_belt_outputs=num_belt_outputs,
        num_pipe_outputs=num_pipe_outputs,
    )

    print(test_machine)

    def test_set_name(self):
        self.assertEqual(self.test_machine.name, self.name)

    def test_set_belt_inputs(self):
        self.assertEqual(self.test_machine.num_belt_inputs, self.num_belt_inputs)

    def test_set_pipe_inputs(self):
        self.assertEqual(self.test_machine.num_pipe_inputs, self.num_pipe_inputs)

    def test_set_belt_outputs(self):
        self.assertEqual(self.test_machine.num_belt_outputs, self.num_belt_outputs)

    def test_set_pipe_outputs(self):
        self.assertEqual(self.test_machine.num_pipe_outputs, self.num_pipe_outputs)

    def test_set_power(self):
        self.assertEqual(self.test_machine.power, self.power)


if __name__ == "__main__":
    unittest.main()
