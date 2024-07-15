def binary_recursive(arr,left,right,number):
    # if right<left:
    #     return -1

    mid = left + right // 2

    if (mid >= len(arr)) or (mid < 0) :
        return -1

    mid_num = arr[mid]

    if mid_num == number:
        return mid

    if mid_num < number:
        return binary_recursive(arr,mid+1,right,number)
    else:
        return binary_recursive(arr,left,mid-1,number)



    return mid


def occurences(arr,number):
    index = binary_recursive(arr,0,0,number)

    indices = []

    # i = index - 1
    # while (i >= 0):
    #     if arr[i] == number:
    #         indices.append(i)
    #     else:
    #         break
    #     i = i - 1

    i = index
    while (i< len(arr)):
        if arr[i] == number:
            indices.append(i)
        else:
            break
        i = i  + 1



    return indices

if __name__ == '__main__':
    array = array = [2,5,8,6,4,6,9,7,6,4,7,9,2,3,4,6]
    print(array)
    array.sort()
    print(array)

    # print(binary_recursive(array, 0, 0, 4))
    print(occurences(array,8))



