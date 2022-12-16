import os

N_PROBLEMS = 25

def create_skeleton_script(path, idx: int):
    skeleton = """from util import read_input_file

if __name__ == "__main__":
    input_date = read_input_file({})
        """.format("\"test_in" + str(idx) + ".txt\"")

    with open(os.path.join(path, str(idx) + ".py"), 'w') as skeleton_file:
        skeleton_file.write(skeleton)

def create_input_files(path, idx: int):
    with open(os.path.join(path, "in" + str(idx) + ".txt"), 'w') as skeleton_file:
        pass

    with open(os.path.join(path, "test_in" + str(idx) + ".txt"), 'w') as skeleton_file:
        pass

def prepare_dirs():
    root_path = os.path.dirname(__file__)
    for idx in range(1, N_PROBLEMS+1):
        new_dir_path = os.path.join(root_path, str(idx))
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
            create_skeleton_script(new_dir_path, idx)
            create_input_files(new_dir_path, idx)


if __name__ == "__main__":
    prepare_dirs()
