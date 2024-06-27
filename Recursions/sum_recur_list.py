def recur_sum(nums_list):
    total = 0
    for element in nums_list:
        # print(element)
        if type(element) == list:
            total = total + recur_sum(element)
        else:
            total = total + element

    return total


print(recur_sum([1, 2, [3,4], [5,6]]))