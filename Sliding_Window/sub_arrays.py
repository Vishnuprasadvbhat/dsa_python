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
def sub_Arr(arr,n,k):
    start = 0
    end = 0
    sum = 0
    mx = 0
    while (end<n):
        if end - start + 1 < k:
            end = end + 1
        if end - start + 1 == k:
            sum = sum + arr[end]
            mx = max(mx,sum)
            sum = sum - arr[start]
            start = start + 1
            end = end +1
    return mx


N = 4
K = 2
Arr = [100, 200, 300, 400]

print(sub_Arr(Arr,N,K))




