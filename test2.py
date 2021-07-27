
set_of_stairs = 0

def solution3(n):
    for first_step in range(1, n//2 + 1):
        build_staircases(first_step, n - first_step)
    return set_of_stairs




def build_staircases(previous_step, remaining_bricks):
    global set_of_stairs
    for value in range(remaining_bricks, previous_step, -1):
        if value == remaining_bricks and value > previous_step:
            set_of_stairs += 1
            continue
        if value > previous_step:
            build_staircases(value, remaining_bricks - value)
