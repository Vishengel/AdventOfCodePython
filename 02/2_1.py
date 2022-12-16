LETTER_TO_INT = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2}
OUTCOME_DICT = {'A': {'X': 3, 'Y': 6, 'Z': 0}, 'B': {'X': 0, 'Y': 3, 'Z': 6}, 'C': {'X': 6, 'Y': 0, 'Z': 3}}
MOVE_SCORE_DICT = {'X': 1, 'Y': 2, 'Z': 3}

def calculate_outcome(opponent, player):
    diff = opponent - player

    if diff == 0:
        return 3
    if diff == 1 or diff == -2:
        return 0
    if diff == 2 or diff == -1:
        return 6

def method1():
    with open('in2.txt') as file:
        sum = 0

        for line in file.readlines():
            stripped_line = line.replace(" ", "").strip("\n")
            sum += calculate_outcome(LETTER_TO_INT[stripped_line[0]], LETTER_TO_INT[stripped_line[1]])
            sum += LETTER_TO_INT[stripped_line[1]] + 1

        print(sum)

def method2():
    with open('in2.txt') as file:
        sum = 0

        for line in file.readlines():
            stripped_line = line.replace(" ", "").strip("\n")
            sum += OUTCOME_DICT[stripped_line[0]][stripped_line[1]]
            sum += MOVE_SCORE_DICT[stripped_line[1]]

        print(sum)

method2()