def sum_n(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_n(nums[1:])


print(sum_n([1,2,3,4,5,6]))