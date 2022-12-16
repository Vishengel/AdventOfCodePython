def get_value_of_letter(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - 38

    return ord(letter) - 96


def print_answer_to_problem1(input):
    sum = 0

    for rucksack in input:
        compartment1 = rucksack[:int(len(rucksack) / 2)]
        compartment2 = rucksack[int(len(rucksack) / 2):]
        common_item = ''.join(set(compartment1).intersection(compartment2))
        sum += get_value_of_letter(common_item)

    print(sum)


def print_answer_to_problem2(input):
    sum = 0

    for idx in range(0, len(input), 3):
        common_item = ''.join(set(input[idx]).intersection(input[idx + 1]).intersection(input[idx + 2]))
        print(common_item)
        sum += get_value_of_letter(common_item)

    print(sum)


with open("in3.txt") as file:
    input = [line.strip('\n') for line in file.readlines()]

print_answer_to_problem1(input)
print_answer_to_problem2(input)
