from itertools import combinations

def exps():
    num_buns = 5
    num_required = 3
    copies_per_key = num_buns - num_required + 1

    sol = [[] for x in range(num_buns)]

    distribution = list(combinations(list(range(num_buns)), copies_per_key))

    current_key = 0
    distribution_index = 0

    while current_key < len(distribution):
        for i in distribution[distribution_index]:
            sol[i].append(current_key)
        current_key +=1
        distribution_index +=1

    return sol