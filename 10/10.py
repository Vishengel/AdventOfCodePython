from util import read_input_file


class CPU:

    def __init__(self):
        self.cycle = 1
        self.X = 1
        self.queue = []
        self.cycle_values = {}
        self.screen = Screen()

    def step(self, instruction: str = None):
        self.cycle_values[self.cycle] = self.X
        if instruction is not None:
            self.parse_instruction(instruction)

        self.screen.determine_pixel_value(self.cycle, self.X)
        self.perform_execution_step()
        self.cycle += 1

    def parse_instruction(self, instruction: str):
        parsed_instruction = instruction.split(" ")

        if len(parsed_instruction) == 2:
            self.queue.append(self.Instruction(int(parsed_instruction[1]), 2))
        else:
            self.queue.append(self.Instruction(0, 1))

    def perform_execution_step(self):
        if len(self.queue) > 0:
            next_instruction = self.queue[0]
            if next_instruction.execute():
                self.X += next_instruction.increment
                self.queue.pop(0)

    def get_signal_strength_per_cycle_number(self, cycle_numbers):
        return {k: k * v for k, v in self.cycle_values.items() if k in cycle_numbers}

    def get_signal_strength_sum(self, cycle_numbers):
        return sum([item[0] * item[1] for item in self.cycle_values.items() if item[0] in cycle_numbers])

    class Instruction:

        def __init__(self, increment, cycle_count):
            self.increment = increment
            self.cycle_count = cycle_count

        def execute(self):
            self.cycle_count -= 1

            if self.cycle_count == 0:
                return True

            return False

        def __str__(self):
            return "({} : {})".format(self.increment, self.cycle_count)


class Screen:

    def __init__(self):
        self.pixels = []

    def determine_pixel_value(self, cycle, X):
        sprite = [X - 1, X, X + 1]
        if (cycle - 1) % 40 in sprite:
            self.pixels.append('#')
        else:
            self.pixels.append('.')

    def print_screen(self):
        for idx, pixel in enumerate(self.pixels):
            if (idx + 1) % 40 == 0:
                print(pixel)
            else:
                print(pixel, end="")


if __name__ == "__main__":
    input_data = read_input_file("in10.txt")
    interesting_cycle_numbers = [20, 60, 100, 140, 180, 220]
    cpu = CPU()

    for instruction in input_data:
        cpu.step(instruction)

    while len(cpu.queue) > 0:
        cpu.step()

    print(cpu.cycle_values)
    print(cpu.get_signal_strength_per_cycle_number(interesting_cycle_numbers))
    print(cpu.get_signal_strength_sum(interesting_cycle_numbers))
    print(cpu.screen.print_screen())
