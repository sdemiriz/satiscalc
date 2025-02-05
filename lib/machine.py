class Machine:

    def __init__(
        self,
        name: str,
        power: float,
        num_belt_inputs: int,
        num_pipe_inputs: int,
        num_belt_outputs: int,
        num_pipe_outputs: int,
    ):
        self.name = name
        self.power = power
        self.num_belt_inputs = num_belt_inputs
        self.num_pipe_inputs = num_pipe_inputs
        self.num_belt_outputs = num_belt_outputs
        self.num_pipe_outputs = num_pipe_outputs

    def __str__(self):
        return f'Machine "{self.name}" uses {self.power} MW and has {self.num_belt_inputs} belt inputs, {self.num_pipe_inputs} pipe inputs and {self.num_belt_inputs} belt inputs, {self.num_pipe_inputs} pipe inputs.'
