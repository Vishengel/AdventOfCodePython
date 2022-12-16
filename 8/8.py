from enum import Enum


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def is_visible_from_direction(forest: [str], original_tree_height: int, tree_coords: tuple, direction: Direction):
    y = tree_coords[0]
    x = tree_coords[1]

    if direction == Direction.NORTH:
        if y - 1 < 0:
            return True
        if forest[y - 1][x] < original_tree_height:
            return is_visible_from_direction(forest, original_tree_height, (y - 1, x), direction)
        return False

    if direction == Direction.EAST:
        if x + 1 >= len(forest[0]):
            return True
        if forest[y][x + 1] < original_tree_height:
            return is_visible_from_direction(forest, original_tree_height, (y, x + 1), direction)
        return False

    if direction == Direction.SOUTH:
        if y + 1 >= len(forest):
            return True
        if forest[y + 1][x] < original_tree_height:
            return is_visible_from_direction(forest, original_tree_height, (y + 1, x), direction)
        return False

    if direction == Direction.WEST:
        if x - 1 < 0:
            return True
        if forest[y][x - 1] < original_tree_height:
            return is_visible_from_direction(forest, original_tree_height, (y, x - 1), direction)
        return False


def is_visible(forest: [str], tree_coords: tuple):
    y = tree_coords[0]
    x = tree_coords[1]

    if is_visible_from_direction(forest, forest[y][x], tree_coords, Direction.NORTH) or \
            is_visible_from_direction(forest, forest[y][x], tree_coords, Direction.EAST) or \
            is_visible_from_direction(forest, forest[y][x], tree_coords, Direction.SOUTH) or \
            is_visible_from_direction(forest, forest[y][x], tree_coords, Direction.WEST):
        return True

    return False


def get_visibility_in_direction(forest: [str], original_tree_height: int, tree_coords: tuple, direction: Direction,
                                viewing_distance: int):
    y = tree_coords[0]
    x = tree_coords[1]

    if direction == Direction.NORTH:
        if y < 0:
            return viewing_distance
        if forest[y][x] >= original_tree_height:
           return viewing_distance + 1

        return get_visibility_in_direction(forest, original_tree_height, (y - 1, x), direction,
                                               viewing_distance + 1)

    if direction == Direction.EAST:
        if x >= len(forest[0]):
            return viewing_distance
        if forest[y][x] >= original_tree_height:
            return viewing_distance + 1

        return get_visibility_in_direction(forest, original_tree_height, (y, x + 1), direction,
                                               viewing_distance + 1)

    if direction == Direction.SOUTH:
        if y >= len(forest):
            return viewing_distance
        if forest[y][x] >= original_tree_height:
            return viewing_distance + 1

        return get_visibility_in_direction(forest, original_tree_height, (y + 1, x), direction,
                                               viewing_distance + 1)

    if direction == Direction.WEST:
        if x < 0:
            return viewing_distance
        if forest[y][x] >= original_tree_height:
            return viewing_distance + 1

        return get_visibility_in_direction(forest, original_tree_height, (y, x - 1), direction,
                                               viewing_distance + 1)


def get_scenic_score(forest: [str], tree_coords: tuple):
    y = tree_coords[0]
    x = tree_coords[1]

    return get_visibility_in_direction(forest, forest[y][x], (y-1, x), Direction.NORTH, 0) * \
           get_visibility_in_direction(forest, forest[y][x], (y, x+1), Direction.EAST, 0) * \
           get_visibility_in_direction(forest, forest[y][x], (y+1, x), Direction.SOUTH, 0) * \
           get_visibility_in_direction(forest, forest[y][x], (y, x-1), Direction.WEST, 0)


if __name__ == "__main__":
    with open("in8.txt") as file:
        forest = [line.strip('\n') for line in file.readlines()]

    n_visible_trees = 2 * len(forest[0]) + 2 * (len(forest) - 2)
    print("Outer ring size: ", n_visible_trees)

    highest_scenic_score = 0

    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest[0]) - 1):
            n_visible_trees += int(is_visible(forest, (y, x)))
            if (scenic_score := get_scenic_score(forest, (y, x))) > highest_scenic_score:
                highest_scenic_score = scenic_score

    print("Total number of visible trees: ", n_visible_trees)
    print("Highest scenic score: ", highest_scenic_score)
