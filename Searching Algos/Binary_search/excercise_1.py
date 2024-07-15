"""Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
This should return 5,6,7 as indices containing number 15 in the array
"""

def binary_recur(arr,left,right,number):
    if right< left:
        return  -1

    mid = left + right //2
    mid_num = arr[mid]

    if mid_num == number:
       return mid_num

    if mid_num < number:
        binary_recur(arr,mid+1,right,number)
    else:
        binary_recur(arr,left,mid-1,number)

    return mid,mid_num



array = [12,34,4,9,8,5,5,5]
print(array)
array.sort()
print(array)

print(binary_recur(array,0,0,5))