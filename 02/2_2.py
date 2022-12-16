OUTCOME_DICT = {'A': {'R': 3, 'P': 6, 'S': 0}, 'B': {'R': 0, 'P': 3, 'S': 6}, 'C': {'R': 6, 'P': 0, 'S': 3}}
MOVE_SCORE_DICT = {'R': 1, 'P': 2, 'S': 3}
DESIRED_OUTCOME_DICT = {'X': 0, 'Y': 3, 'Z': 6}

def get_move(opponent_move, desired_outcome):
    for key, value in OUTCOME_DICT[opponent_move].items():
        if value == desired_outcome:
            return key

def get_score(opponent_move, desired_outcome_as_char):
    desired_outcome = DESIRED_OUTCOME_DICT[desired_outcome_as_char]
    move = get_move(opponent_move, desired_outcome)
    return desired_outcome + MOVE_SCORE_DICT[move]

with open('in2.txt') as file:
    sum = 0

    for line in file.readlines():
        stripped_line = line.replace(" ", "").strip("\n")
        sum += get_score(stripped_line[0], stripped_line[1])

    print(sum)
