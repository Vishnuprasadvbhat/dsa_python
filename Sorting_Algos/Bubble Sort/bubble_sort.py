nums = [1,3,4,78,975,335,55,66,85,22]


def bubble_sort(elements):
    size = len(elements)
    for i in range(size-1):
        swapped= False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
    return elements



print(bubble_sort(nums))
