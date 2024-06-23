from array import * 

a= array('i',[23,34,56])

print(type(a))

for _ in a:
  print(_)

# for i in range(3):
#   print(a[i], end=' ')

i = 0
while(i<len(a)):
  print(a[i])
  i+=1
b= array('i', [2,3,4,5])

print(a.count(5))
print(a.extend(b))
print(b)
print(a)

from  numpy import *
import numpy as np

arr = np.array(['hello','how', 'are', 'you? ']) # 1D array 
print(len(arr))

# 2D array with same numbers of elements 
arr2= np.array([1,2,3], [4,5,6]) 

#1D array with two elements
arr3 = np.array([1,2,3],[1,2]) 


