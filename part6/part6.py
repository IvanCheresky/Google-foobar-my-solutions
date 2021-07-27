import math
from decimal import Decimal, getcontext


def solution(str_n):
    return str(sol_int(int(str_n)))


def sol_int(n):
    getcontext().prec = 101
    if n == 0:
        return 0
