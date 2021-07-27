from itertools import permutations

# origins_1 = set(permutations([1, 0, 0, 0], 4))
# origins_0 = set(permutations([0, 0, 0, 0], 4)) | set(permutations([1, 1, 0, 0], 4)) \
#             | set(permutations([1, 1, 1, 0], 4)) | set(permutations([1, 1, 1, 1], 4))
# origins_0 = [list(x) for x in origins_0]
# origins_1 = [list(x) for x in origins_1]

origins_0 = {(0, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 1, 0), (0, 1, 1, 0), (1, 0, 1, 0), (0, 0, 0, 0), (1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 1, 1), (1, 1, 1, 1)}
origins_1 = {(0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)}


def solution(g):

    column_0 = create_column([x[0] for x in g])
    column_0.create_right_dict()

    last_consolidation = column_0.right_dic

    for i in range(1, len(g[0])):
        column = create_column(tuple(x[i] for x in g))
        last_consolidation = consolidate(last_consolidation, column)

    print(sum(last_consolidation.values()))
    return sum(last_consolidation.values())


def consolidate(first_col, second_col):
    consolidated = dict()

    for first_col_comb, value in first_col.items():
        for second_col_comb in second_col.combs:
            if check_equal_columns(first_col_comb, second_col_comb):
                new_right_column = tuple(x for i, x in enumerate(second_col_comb) if i % 2 != 0)
                if new_right_column in consolidated:
                    consolidated[new_right_column] += value
                else:
                    consolidated[new_right_column] = value

    return consolidated


def check_equal_columns(first, second):
    for i in range(len(first)):
        if first[i] != second[i*2]:
            return False
    return True


def create_column(arr):
    column = Column()
    if arr[0] == 0:
        column.add_initial(origins_0)
    else:
        column.add_initial(origins_1)

    for value in arr[1:]:
        if value == 0:
            column.add(origins_0)
        else:
            column.add(origins_1)
        column.commit()

    return column


class Column:
    def __init__(self):
        self.combs = []
        self.new_combs = []
        self.right_dic = dict()
        self.left_dic = dict

    def add_initial(self, combs):
        for comb in combs:
            self.combs.append(comb)

    def add(self, combs_to_add):
        for comb in self.combs:
            for comb_to_add in combs_to_add:
                if comb[-2] == comb_to_add[0] and comb[-1] == comb_to_add[1]:
                    self.new_combs.append(list(comb) + [comb_to_add[2], comb_to_add[3]])

    def commit(self):
        self.combs = self.new_combs
        self.new_combs = []

    def create_right_dict(self):
        for comb in self.combs:
            right = tuple(x for i, x in enumerate(comb) if i % 2 != 0)
            if right in self.right_dic:
                self.right_dic[right] += 1
            else:
                self.right_dic[right] = 1
