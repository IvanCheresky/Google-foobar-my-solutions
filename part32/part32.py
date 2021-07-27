import random
from copy import deepcopy

paths = []
min_path = float('inf')
least_possible = 0
grid_after_removals = [[]]
grid_before_removals = [[]]

def test_with_random_grid():
    height = random.randrange(2, 20)
    width = random.randrange(2, 20)

    grid = []
    for i in range(height+1):
        grid.append([0 if random.randrange(0, 100) < 80 else 1 for x in range(width+1)])

    grid[0][0] = 0
    grid[-1][-1] = 0

    for i in grid:
        print(f"{i},")

    print(solution6([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))



def solution6(map):
    global grid_after_removals
    global grid_before_removals

    grid_after_removals = [[float('inf') for x in map[0]] for y in map]
    grid_before_removals = [[float('inf') for x in map[0]] for y in map]

    global least_possible
    global paths
    least_possible = len(map) + len(map[0])
    paths.append(Path(False, [[0,0]]))

    while paths:
        path = paths.pop()

        if len(path.path) >= min_path:
            del path
            continue

        if can_go_left(map, path):
            move(map, path, 0, -1)

        if can_go_right(map, path):
            move(map, path, 0, 1)

        if can_go_up(map, path):
            move(map, path, -1, 0)

        if can_go_down(map, path):
            move(map, path, 1, 0)

        del path

        if min_path == least_possible:
            return min_path

    return min_path


def move(map, path, y, x):
    global min_path
    global paths
    if is_inefficient_path(map, path, y, x):
        return
    new_path = deepcopy(path)
    new_path.path.append([path_to_y_coord(path) + y, path_to_x_coord(path) + x])
    if is_on_1(map, new_path):
        new_path.used_removal = True
    if is_at_exit(map, new_path):
        if min_path > len(new_path.path):
            min_path = len(new_path.path)
        del new_path
    else:
        paths.append(new_path)


def is_inefficient_path(map, path, y, x):
    if path.used_removal:
        if grid_after_removals[path_to_y_coord(path) + y][path_to_x_coord(path) + x] <= len(path.path) + 1:
            return True
        else:
            grid_after_removals[path_to_y_coord(path) + y][path_to_x_coord(path) + x] = len(path.path) + 1
            return False
    else:
        if grid_before_removals[path_to_y_coord(path) + y][path_to_x_coord(path) + x] <= len(path.path) + 1:
            return True
        else:
            grid_before_removals[path_to_y_coord(path) + y][path_to_x_coord(path) + x] = len(path.path) + 1
            return False


# check if the x-coordinate of the current coordinates is zero (in that case, can't go left)
# check if there is a zero to the left or if there is a removal remaining
# check if already in path
def can_go_left(map, path):
    if path_to_x_coord(path) != 0:
        if (map[path_to_y_coord(path)][path_to_x_coord(path)-1] == 0 or not path.used_removal) and \
                ([path_to_y_coord(path), path_to_x_coord(path)-1] not in path.path):
            return True
    return False

# same for right
def can_go_right(map, path):
    if path_to_x_coord(path) != len(map[0]) - 1:
        if (map[path_to_y_coord(path)][path_to_x_coord(path)+1] == 0 or not path.used_removal) and \
                ([path_to_y_coord(path), path_to_x_coord(path)+1] not in path.path):
            return True
    return False

# same for up
def can_go_up(map, path):
    if path_to_y_coord(path) != 0:
        if (map[path_to_y_coord(path) - 1][path_to_x_coord(path)] == 0 or not path.used_removal) and \
                ([path_to_y_coord(path) - 1, path_to_x_coord(path)] not in path.path):
            return True
    return False

# same for down
def can_go_down(map, path):

    if path_to_y_coord(path) != len(map) - 1:
        if (map[path_to_y_coord(path) + 1][path_to_x_coord(path)] == 0 or not path.used_removal) and \
                ([path_to_y_coord(path) + 1, path_to_x_coord(path)] not in path.path):
            return True
    return False


# returns the y-coord of the last coord n the path
def path_to_y_coord(path):
    return path.path[-1][0]

# returns the x-coord of the last coord n the path
def path_to_x_coord(path):
    return path.path[-1][1]

# returns whether the Path is currently on a 1
def is_on_1(map, path):
    return map[path_to_y_coord(path)][path_to_x_coord(path)] == 1

#check if we are at the exit
def is_at_exit(map, path):
    return [path_to_y_coord(path), path_to_x_coord(path)] == [len(map) - 1, len(map[0]) - 1]

class Path():
    def __init__(self, used_removal, arr):
        self.used_removal = used_removal
        self.path = arr

