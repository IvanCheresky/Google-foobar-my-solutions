# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import operator
import random
import cProfile
from itertools import combinations

from part6.part6 import solution


def solution2(l):
    spl = [x.split(".") for x in l]

    for arr in spl:
        if len(arr) == 1:
            arr.append(-1)
            arr.append(-1)
        if len(arr) == 2:
            arr.append(-1)

    sorted_list = sorted(spl, key=operator.itemgetter(0))

    ranges_to_sort = sub_array_to_be_sorted(0, sorted_list)

    for r in ranges_to_sort:
        sorted_list[r[0]:r[1]] = (sorted(sorted_list[r[0]:r[1]], key=lambda x: int(operator.itemgetter(1)(x))))

    ranges_to_sort = sub_array_to_be_sorted(1, sorted_list)
    for r in ranges_to_sort:
        sorted_list[r[0]:r[1]] = (sorted(sorted_list[r[0]:r[1]], key=lambda x: int(operator.itemgetter(2)(x))))

    for index, arr in enumerate(sorted_list):
        sorted_list[index] = [x for x in arr if x != -1]
        sorted_list[index] = ".".join(sorted_list[index])

    return sorted_list


def sub_array_to_be_sorted(version, sorted_list):
    start = 0
    end = 0
    previous_num = sorted_list[0][version]
    ranges_to_sort = []
    for index, arr in enumerate(sorted_list):
        if arr[version] == previous_num:
            end = index
        else:
            if start != end:
                ranges_to_sort.append([start, end + 1])
            start = index
            end = index
        previous_num = arr[version]
    if start != end:
        ranges_to_sort.append([start, end + 1])

    return ranges_to_sort


def test():
    a = [['0', '1'], ['1', '11'], ['1', '2'], ['1', '2', '1'], ['1', '1', '1'], ['2', '0', '0'], ['2'], ['2', '0']]
    print(a[1:4])
    print(a)

    arr = [random.randrange(1, 50) for x in range(random.randrange(1500, 1600))]

if __name__ == "__main__":
    print(solution('77'))