def fib(n):
    if n==0 or n==1:
        return n

    for i in range(n):
        res = fib(n-1) + fib(n-2)
        return res

if __name__ == '__main__':
    print(fib(4))