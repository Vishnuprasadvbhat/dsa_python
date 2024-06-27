def postive_integer(n):
    if n<=1:
        return n
    return n + postive_integer(n-2)


print(postive_integer(6))
print(postive_integer(10))
