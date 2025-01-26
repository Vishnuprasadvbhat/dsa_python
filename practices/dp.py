# array  = [8,9,7,5,2,8,4,1,6,8,3]

# unique = set()

# for num in array:
#   unique.add(num)

# print(array)
# print(unique)

# unique_ele = list(set(array))
# print(unique_ele)

# unique_same = list(dict.fromkeys(array))
# print(unique_same)

def fib(n):
  if n== 0:
    return 0
  
  if n == 1:
    return 1

  return fib(n-1) + fib(n-2)

print(fib(5))

def fibonacci(n):
    fib_seq = [0, 1]  # Start the sequence with 0 and 1
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[:n]

# Example usage
n = 10  # Number of Fibonacci numbers to generate
print(fibonacci(n))


number = 100
number = number // 10 
rem = number % 10 
new_num = rem 
print(number)
print(new_num)


def reversed_num(n):
  rev_num = 0

  while n != 0:
    rem = n % 10
    rev_num = rev_num *10 + rem
    n = n //10 

  return rev_num

print(reversed_num(2506))