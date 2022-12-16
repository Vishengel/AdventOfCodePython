def print_answer_to_problem1():
    count = 0

    with open("in4.txt") as file:
        for line in file.readlines():
            pair = line.split(',')
            left1 = int(pair[0].split('-')[0])
            right1 = int(pair[0].split('-')[1])
            left2 = int(pair[1].split('-')[0])
            right2 = int(pair[1].split('-')[1])

            if (left1 >= left2 and right1 <= right2) or (left2 >= left1 and right2 <= right1):
                count += 1

    print(count)


def print_answer_to_problem2():
    count = 0

    with open("in4.txt") as file:
        for line in file.readlines():
            pair = line.split(',')
            left1 = int(pair[0].split('-')[0])
            right1 = int(pair[0].split('-')[1])
            left2 = int(pair[1].split('-')[0])
            right2 = int(pair[1].split('-')[1])

            if not (right1 < left2 or left1 > right2 or right2 < left1 or left2 > right1):
                count += 1

    print(count)


print_answer_to_problem1()
print_answer_to_problem2()
