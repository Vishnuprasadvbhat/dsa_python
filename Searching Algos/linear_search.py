def linear(arr, N, key):
    # N = int(input('Enter the size of array: '))
    arr = []
    for i in range(0, N):
        values = int(input("enter the Array values: "))
        arr.append(values)
    print(arr)

    for index, element in enumerate(arr):
        if element == key:
            return (f'The element {element} is at index {index}')
    return False


print(linear([],5,5))