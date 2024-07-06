# this is right Shift where we remove 0's to right
# in right shift we divide the num by 2
num = 100
print('num: ',num)
form = bin(num)[2:]
print(form)
print('------------------')


num1 = num >> 1
print('num1: ',num1)
form1 = bin(num1)[2:]
print(form1)

print('------------------')


num2 = num << 1
print('num2: ',num2)
form2 = bin(num2)[2:]
print(form2)
