class Rope:

    def __init__(self, n_segments):
        self.n_segments = n_segments
        self.rope_segments = {k: (0, 0) for k in range(0, n_segments + 1)}
        self.visited = {self.rope_segments[n_segments]}

    def execute_motion(self, motion: str):
        print(motion)
        direction, n_steps = motion.split(" ")

        for x in range(int(n_steps)):
            self.step_in_direction(direction)
            self.visited.add(self.rope_segments[self.n_segments])

    def step_in_direction(self, direction: str):
        self.move_head(direction)

        for idx in range(1, self.n_segments + 1):
            self.rope_segments[idx] = self.move_rope(self.rope_segments[idx - 1], self.rope_segments[idx])

        print(self)

    def move_head(self, direction: str):
        head = self.rope_segments[0]

        if direction == 'U':
            head = (head[0] - 1, head[1])
        elif direction == 'R':
            head = (head[0], head[1] + 1)
        elif direction == 'D':
            head = (head[0] + 1, head[1])
        elif direction == 'L':
            head = (head[0], head[1] - 1)

        self.rope_segments[0] = head

    def move_rope(self, lead_pos, follow_pos):
        dy = lead_pos[0] - follow_pos[0]
        dx = lead_pos[1] - follow_pos[1]

        if abs(dy) == 2:
            follow_pos = (follow_pos[0] + dy // 2, follow_pos[1])
            if abs(dx) == 1:
                follow_pos = (follow_pos[0], follow_pos[1] + dx)
        if abs(dx) == 2:
            follow_pos = (follow_pos[0], follow_pos[1] + dx // 2)
            if abs(dy) == 1:
                follow_pos = (follow_pos[0] + dy, follow_pos[1])

        return follow_pos

    def __str__(self):
        return "Rope: {}".format(self.rope_segments)


if __name__ == "__main__":
    with open("in9.txt") as file:
        input_data = [line.strip('\n') for line in file.readlines()]

    print(input_data)

    rope = Rope(9)

    for motion in input_data:
        rope.execute_motion(motion)

    print(len(rope.visited))