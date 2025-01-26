
# The approach must be dividing a problem into sub-problems and then building the logic on top of it

# Implementing quick sort

def swap_it(a,b,arr):
    if a != b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
def partition(elements):

    pivot_index = 0
    pivot = elements[pivot_index]

    left = pivot_index + 1
    right = len(elements)-1

    while elements[left] <= pivot:
        left += 1

    while elements[right] > pivot:
        right -= 1


    # perform swaping if left < right
    if left < right:
        swap_it(left,right,elements)

    return elements
def quick_sort():

    pass

if __name__ == "__main__":
    elements = [11, 2, 3, 4, 5, 677, 8, 9, 77]

    # print(quick_sort(elements))
    print(elements)
    print(partition(elements))
