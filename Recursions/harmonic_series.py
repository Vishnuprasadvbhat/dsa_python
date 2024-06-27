def harmonic(n):
    if n< 2:
        return n
    for i in range(n):
        return 1 / n + harmonic(n-1)

print(round(harmonic(4)))