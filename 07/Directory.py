class Directory:

    def __init__(self, name: str, parent_dir):
        self.parent_dir = parent_dir
        self.children = {}
        self.files = {}
        self.name = name
        self.size = 0
        self.set_path()

    def is_root_dir(self):
        return self.parent_dir is None

    def set_path(self):
        if self.is_root_dir():
            self.path = '/'
        else:
            self.path = self.parent_dir.path + self.name + '/'

    def add_child(self, name):
        self.children[name] = Directory(name, self)

    def add_file(self, name, size):
        self.files[name] = int(size)
        self.propagate_size(int(size))

    def propagate_size(self, size: int):
        self.size += size

        if self.is_root_dir():
            return

        self.parent_dir.propagate_size(size)

    def get_dirs_with_max_size(self, dirs: dict, max_size: int):
        if self.size <= max_size:
            dirs[self.path] = self.size

        for child in self.children.values():
            child.get_dirs_with_max_size(dirs, max_size)

        return dirs

    def get_dirs_with_min_size(self, dirs: dict, min_size: int):
        if self.size >= min_size:
            dirs[self.path] = self.size

        for child in self.children.values():
            child.get_dirs_with_min_size(dirs, min_size)

        return dirs

    def print_subtree(self):
        print("Current dir: ", self.path)
        print("Dir size: ", self.size)
        print("Dirs: ", [child.name for child in self.children.values()])
        print("Files: ", self.files)
        print("-------")

        for child in self.children.values():
            child.print_subtree()