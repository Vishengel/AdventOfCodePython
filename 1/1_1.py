import numpy as np

def read_calories_from_input():
    calorie_count_list = []
    calorie_sum = 0

    with open("in1_1_dorieke.txt") as file:
        for line in file.readlines():
            if line in ['\n', '\r\n']:
                calorie_count_list.append(calorie_sum)
                calorie_sum = 0
            else:
                calorie_sum += int(line.strip('\n'))

    return calorie_count_list

def get_n_most_loaded_elfs(calorie_count_list, n):
    sorted_list = sorted(calorie_count_list, reverse=True)
    return (sorted_list[:n])

if __name__ == "__main__":
    calorie_count_list = read_calories_from_input()
    print(calorie_count_list)
    print("Elf {} is carrying {} calories".format(np.argmax(calorie_count_list) + 1, max(calorie_count_list)))
    print(sum(get_n_most_loaded_elfs(calorie_count_list, 3)))