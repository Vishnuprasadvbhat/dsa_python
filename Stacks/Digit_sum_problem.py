lst = [22,45,36,78,890,12]
stack_data  = []

def Find_Min(num):
    min = 9
    while(num!=0):
        r =num%10
        min = r if r<min else min
        num//=10
    return min

print(sum(Find_Min(i) for i in lst))