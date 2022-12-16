def read_input_file(input_file):
    with open(input_file) as file:
        input_data = [line.strip('\n') for line in file.readlines()]

    return input_data