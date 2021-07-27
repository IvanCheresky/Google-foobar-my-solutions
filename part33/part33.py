def solution7(l):

    solutions = 0

    for index, value in enumerate(l):
        for index2, value2 in enumerate(l[index + 1:]):
            if value2 % value != 0:
                continue
            for index3, value3 in enumerate(l[index + index2 + 2:]):
                if value3 % value2 == 0 and value2 % value == 0:
                    solutions += 1

    return solutions


def solution8(l):
    total = 0

    grid = [[False for x in l] for x in l]

    for index, value in enumerate(l):
        for index2, value2 in enumerate(l):
            if index2 > index and value2 % value == 0:
                grid[index][index2] = True

    for index, y in enumerate(grid):
        for index2, x in enumerate(y):
            if x is True:
                for val in grid[index2]:
                    if val is True:
                        total +=1

    return total

def solution9(l):
    total = 0
    number_of_divisors = [0 for x in l]

    for index, value in enumerate(l):
        for index2, value2 in enumerate(l[:index]):
            if value % value2 == 0:
                number_of_divisors[index] += 1
                total += number_of_divisors[index2]
    print(number_of_divisors)
    return total
