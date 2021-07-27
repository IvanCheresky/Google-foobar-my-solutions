
set_of_stairs = []

def solution2(n):
    for first_step in range(1, n//2 + 1):
        arr = [first_step]
        build_staircases(arr, n - first_step)

    for arr in set_of_stairs:
        if set_of_stairs.count(arr) > 1:
            print(f"duplicate {arr}")
    return sorted(set_of_stairs)


def build_staircases(arr, remaining_bricks):
    global set_of_stairs
    for value in range(remaining_bricks, arr[-1], -1):
        if value == remaining_bricks and value > arr[-1]:
            arr2 = arr.copy()
            arr2.append(value)
            set_of_stairs.append(arr2)
            continue
        if value > arr[-1]:
            arr2 = arr.copy()
            arr2.append(value)
            build_staircases(arr2, remaining_bricks - value)

