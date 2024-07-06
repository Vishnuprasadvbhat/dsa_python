
# this is left Shift where we add 0's to right
# in left shift we multiply the num by 2

num = 10
# print(bin(num)[2:])
output = bin(num)[2:].zfill(32)
print(output)


#zfill function adds zeros to the prefix position of the bin form
#bin returns binary form of decimal
#  '<<' is used for left shift operation in the bitwise algos


num = num << 1
print('NUM: ', num)
output = bin(num)[2:].zfill(32)
print(output)

