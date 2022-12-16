from Directory import Directory

TOTAL_DISK_SPACE = 70000000
REQUIRED_SPACE = 30000000

def build_file_tree(instructions: [str]):
    root_dir = Directory('/', None)
    current_dir = root_dir

    for instruction in instructions[1:]:
        if "$ cd" in instruction:
            target_dir = instruction.split(" ")[2]
            if target_dir == "..":
                current_dir = current_dir.parent_dir
            else:
                current_dir.add_child(target_dir)
                current_dir = current_dir.children[target_dir]
        elif instruction[0].isdigit():
            # Files start with an integer size
            file_size, file_name = instruction.split(" ")
            current_dir.add_file(file_name, file_size)

    return root_dir

def problem1(tree_root_dir):
    small_dirs = tree_root_dir.get_dirs_with_max_size({}, 100000)

    print("\nProblem 1:")
    print("===========")
    print("Dirs smaller than or equal to 100,000 bytes: ", small_dirs)
    print("Sum of dirs smaller than 100,000 bytes: ", sum([size for size in small_dirs.values()]))

def problem2(tree_root_dir):
    free_space = TOTAL_DISK_SPACE - tree_root_dir.size
    space_to_be_freed = REQUIRED_SPACE - free_space
    candidate_dirs = tree_root_dir.get_dirs_with_min_size({}, space_to_be_freed)

    print("\nProblem 2:")
    print("===========")
    print("Dirs larger than or equal to {} bytes: {}".format(space_to_be_freed, candidate_dirs))
    print("Size of smallest candidate dir: ", min(candidate_dirs.values()))

if __name__ == "__main__":
    with open("in7.txt") as file:
        instructions = [line.strip('\n') for line in file.readlines()]

    tree_root_dir = build_file_tree(instructions)
    tree_root_dir.print_subtree()
    problem1(tree_root_dir)
    problem2(tree_root_dir)
