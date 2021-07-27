
def solution4(n):
    total = 0
    for i in range(1,n):
        total += sc(i, n-i)

    return total

def sc(prev, rem):
    total = 0

    for j in range(prev+1, rem+1):
        if j > prev and j == rem:
            total +=1
        if j > prev and j < rem:
            total += sc(j, rem-j)

    return total