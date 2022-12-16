def find_marker(input_data: str, window_size: int):
    for idx in range(len(input_data) - (window_size - 1)):
        window = input_data[idx:idx + window_size]
        if len(set(window)) == len(window):
            return idx + window_size


if __name__ == "__main__":
    with open("in6.txt") as input:
        input_data = input.readlines()[0]

    print(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4))
    print(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4))
    print(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 4))
    print(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4))
    print(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4))
    print(find_marker(input_data, 4))

    print(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14))
    print(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14))
    print(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14))
    print(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14))
    print(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14))
    print(find_marker(input_data, 14))