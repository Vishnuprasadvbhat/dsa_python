def sum_non(n):
    if n<=1:
        return n
    return n%10 + sum_non(int(n/10))


print(sum_non(325))
print(sum_non(45))
print(sum_non(75))
print(sum_non(125))
