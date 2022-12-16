STACK_IDX_LINE = 8
INSTRUCTIONS_START_LINE = 10
N_STACKS = 9


def get_initial_stacks(input: list):
    stack_indices_line = input[STACK_IDX_LINE]
    stack_indices = [stack_indices_line.index(str(idx)) for idx in range(1, N_STACKS + 1)]
    stacks = {idx: [] for idx in range(1, N_STACKS + 1)}

    for row in input[:STACK_IDX_LINE]:
        for idx, idx_line_position in enumerate(stack_indices):
            if idx_line_position < len(row) and row[idx_line_position].isalpha():
                stacks[idx + 1].append(row[idx_line_position])

    return stacks


def print_stacks_rowwise(stacks: dict):
    for k, v in stacks.items():
        print("{}.{}".format(k, ''.join(v)))


def parse_instruction(instruction: str):
    amount_string, stack_numbers_string = instruction.split('from')
    amount = int(''.join([n for n in amount_string if n.isdigit()]))
    stacks_numbers = [int(n) for n in stack_numbers_string if n.isdigit()]

    return amount, stacks_numbers[0], stacks_numbers[1]


def get_final_result(input: list, is_cratemover_9000: bool = True, debug: bool = False):
    stacks = get_initial_stacks(input)

    if debug:
        print_stacks_rowwise(stacks)

    for instruction in input[INSTRUCTIONS_START_LINE:]:
        amount, start, end = parse_instruction(instruction)

        if is_cratemover_9000:
            stacks[end] = stacks[start][:amount][::-1] + stacks[end]
        else:
            stacks[end] = stacks[start][:amount] + stacks[end]

        stacks[start] = stacks[start][amount:]

        if debug:
            print("-----------------------------")
            print(instruction, end="")
            print("-----------------------------")
            print_stacks_rowwise(stacks)

    return stacks


if __name__ == "__main__":
    with open("in5.txt") as file:
        input = file.readlines()

    final_stacks = get_final_result(input, False, False)
    print(''.join([stack[0] for stack in final_stacks.values()]))
