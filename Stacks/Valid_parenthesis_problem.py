# Given a string s containing just the char "

#constrains

string = str(input('Enter the string: '))
stack = []
valid = [')','}',']']
count = 0
for i in string:
    if i not in valid:
        count += 1
        stack.append(i)
        # print(stack)

    else:
        stack.pop()
        count -= 1
        # print(stack)
else:
    print('Invaid string input')

if count == 0:
    print(True)
    print(count)
else:
    print(False)
    print('Invalid string input')

    # print(stack)

# This does not pass all test cases need to update the code
