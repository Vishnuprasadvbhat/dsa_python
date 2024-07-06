#


#Setting of the bit for given number
def setBit(num,pos):
    num |= (1<<pos)
    print(num)


num = 4
pos = 1

setBit(num,pos)
setBit(5,1)

#Unsetting of the bit for given number

def unset(num,pos):
    num &= (~(1 << pos))
    print(num)

unset(7,1)

# toggling using XOR - Symbol '^'

def toggle_xor(num,pos):
    num ^= (1<<pos)
    print(num)

toggle_xor(7,1)


#check the bit is set or unset:

def check_set()