def gp_series(n):
    if n<2:
        return n

    return 1/ pow(2,n) + gp_series((n-1))



print(gp_series(3))