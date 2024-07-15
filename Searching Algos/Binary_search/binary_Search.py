def binary_search(arr,number_to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_num = arr[mid]
        if mid_num == number_to_find:
            return mid,mid_num
        if mid_num < number_to_find:
            left = mid + 1
        else:
            right = mid - 1
    return -1


print(array)
x = 12
print(binary_search(array,x))
