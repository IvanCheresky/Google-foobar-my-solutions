# staircases problem

def solution5(n):
    gen_fun = [1 if x < 2 else 0 for x in range(n + 1)]

    for i in range(2, n+1):
        for j in range(n, i-1, -1):
            gen_fun[j] = gen_fun[j] + gen_fun[j-i]
    return gen_fun[n] - 1
