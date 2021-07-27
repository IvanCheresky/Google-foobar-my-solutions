# THIS IS THE SOLUTION

from copy import deepcopy


def solution12(times, times_limit):

    # modified bellman ford, modifies times to express the shortest paths to each vertex
    for i in range(len(times)):
        for index, vertex in enumerate(times):
            for index2, edge in enumerate(times[index]):
                # times[0][index] is an edge in the start vertex
                for index3, edge2 in enumerate(times[index]):
                    times[index][index2] = min(times[index][index2], times[index][index3] + times[index3][index2])


    # check for infinite negative loops
    for i in range(len(times)):
        if times[i][i] < 0:
            return[x for x in range(len(times) - 2)]

    map = dict()

    # check all paths
    paths = [Path(len(times), 0, times_limit)]
    possible_solutions = []

    while paths:
        path = paths.pop()
        for index, edge in enumerate(times[path.current_vertex]):
            print(map)
            if path.current_vertex == index:
                continue

            new_path = deepcopy(path)
            new_path.passed_through_vertex(index)
            new_path.current_vertex = index
            new_path.remaining_time -= edge

            if (index, tuple(new_path.bunnies_rescued)) not in map or map[(index, tuple(new_path.bunnies_rescued))] < new_path.remaining_time:

                map[(index, tuple(path.bunnies_rescued))] = new_path.remaining_time
                paths.append(new_path)

                if new_path.current_vertex == len(times) - 1 and new_path.remaining_time >= 0:
                    possible_solutions.append(new_path.bunnies_rescued[:])


    possible_solutions.sort()

    solution = []

    for sol in possible_solutions:
        if len(sol) > len(solution):
            solution = sol

    return sorted(solution)


class Path:
    def __init__(self, number_of_vertex, current_vertex, remaining_time):
        self.bunnies_rescued = []
        self.number_of_vertex = number_of_vertex
        self.current_vertex = current_vertex
        self.remaining_time = remaining_time

    def passed_through_vertex(self, vertex):
        if 0 < vertex < self.number_of_vertex - 1 and vertex - 1 not in self.bunnies_rescued:
            self.bunnies_rescued.append(vertex - 1)
            self.bunnies_rescued.sort()