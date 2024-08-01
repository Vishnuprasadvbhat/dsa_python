array =[1,3,3,4,5,6,6]

prefix= [0 for i in range(len(array))]



for i in range (0,len(array)):
    prefix[i] = prefix[i-1] + array[i]

print(prefix)