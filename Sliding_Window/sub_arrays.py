"""
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Example:
Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum. .
"""
def sub_arr(arr,k):
    n= len(arr)

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for  i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum,window_sum)

    return max_sum



# N = 4
K = 2
Arr = [100, 200, 300, 400]

print(sub_arr(Arr,K))




