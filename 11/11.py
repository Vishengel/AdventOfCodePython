from util import read_input_file


class Monkey:

    def __init__(self, name):
        self.name = name
        self.items = []

    def give_item(self, item: int):
        self.items.append(item)

    def set_operation(self, operator: str, term2: str):
        self.operator = operator
        self.operator_term2 = term2

    def set_test_term(self, test_term: int):
        self.test_term = test_term

    def set_target_true(self, target_true: int):
        self.target_true = target_true

    def set_target_false(self, target_false: int):
        self.target_false = target_false

    def __str__(self):
        return """Monkey {}:
  Starting items: {}
  Operation: new = old {} {}
  Test: divisible by {}
    If true: throw to monkey {}
    If false: throw to monkey {}
        """.format(self.name, self.items, self.operator, self.operator_term2, self.test_term, self.target_true,
                   self.target_false)


class Game:

    def __init__(self, input_data: [str]):
        self.monkeys = self.parse_monkeys(input_data)

    def parse_monkeys(self, input_data: [str]):
        monkeys = {}
        new_monkey = None

        for line in input_data:
            cleaned_line = line.strip(' ').lower().replace(',', '').replace(':', '')
            tokens = cleaned_line.split(' ')
            if cleaned_line.startswith("monkey"):
                new_monkey = Monkey(tokens[1])
            elif "items" in cleaned_line:
                items = tokens[2:]
                for item in items:
                    new_monkey.give_item(int(item))
            elif "operation" in cleaned_line:
                new_monkey.set_operation(tokens[4], tokens[5])
            elif "test" in cleaned_line:
                new_monkey.set_test_term(int(tokens[3]))
            elif "true" in cleaned_line:
                new_monkey.set_target_true(int(tokens[5]))
            elif "false" in cleaned_line:
                new_monkey.set_target_false(int(tokens[5]))

            if new_monkey is not None:
                monkeys[new_monkey.name] = new_monkey

        return monkeys


if __name__ == "__main__":
    input_data = read_input_file("test_in11.txt")
    game = Game(input_data)
    for monkey in game.monkeys.values():
        print(monkey)
