import copy
import math
from itertools import combinations

# THE ACTUAL SOLUTION IS IN EXPERIMENTS

def solution(num_buns, num_required):
    # the amount of bunnies without any given number must be equal to the number of bunnies required minus 1
    skips = num_required - 1

    if skips == 0:
        return [[0] for i in range(num_buns)]

    # the number of keys must be such that the total amount of skipped keys is a multiple of the number of bunnies
    keys = 1
    keys = int(lcm(skips*keys, num_buns)/skips)

    print(make_skip_list(keys, num_buns, skips))
    breakpoint()

    # the number of missing keys per bunny must guarantee that it is not possible with less than the number required:
    # quantity of keys combination missing keys per bunny must be at least num of buns
    print(f"nCr({keys}, {skips * keys} / {num_buns}) < num_buns")
    print(nCr(keys, skips * keys / num_buns))
    while nCr(keys, skips * keys / num_buns) < num_buns:
        keys = lcm(skips * (keys + 1), num_buns)


    sol = []

    return sorted(sol)


def make_skip_list(keys, num_buns, skips):
    keys = keys*2
    skips_per_bun = int(skips * keys / num_buns)
    skips_per_bun = 4
    coms = list(combinations(range(keys-1,-1,-1), skips_per_bun))

    print(coms)
    valid_list = []

    skip_list_list = [SkipList(keys, skips)]

    while skip_list_list:
        skip_list = skip_list_list.pop()
        for index in range(skip_list.index, len(coms)):
            print(skip_list.list_of_skips)
            if skip_list.can_add_skip(coms[index]):
                skip_list_copy = copy.deepcopy(skip_list)
                skip_list_copy.index = index + 1
                skip_list_list.append(skip_list_copy)
                skip_list.add_skip(coms[index])
                if skip_list.is_complete():
                    print(skip_list)
                    break

    print(valid_list)



class SkipList:
    def __init__(self, keys, repetitions):
        self.keys = keys
        self.repetitions = repetitions
        self.skips_per_key = dict()
        self.list_of_skips = []
        self.index = 0
        for i in range(keys):
            self.skips_per_key[i] = 0

    def can_add_skip(self, skips):
        for i in skips:
            if self.skips_per_key[i] > self.repetitions:
                return False

        return True

    def add_skip(self, skips):
        for i in skips:
            self.skips_per_key[i] += 1

        self.list_of_skips.append(skips)

    def is_complete(self):
        for i in self.skips_per_key.values():
            if i != self.repetitions:
                return False
        return True



def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)