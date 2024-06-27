def fac(n):
    if n == 0 or n==1:
        return n

    return n * fac(n - 1)

print(fac(6))