""" Collision occurs when a key tries to save its values in the location
 where a value already exists, resulting in Collision due to same index

 This problem can be solved by using few approaches:
 1. Chaining: creating a Linked List to save the new values
    problems:
        1. traversal increases and O(1)
        2. Bad matching function results in saving to same index
 2. Linear Probing: This approaches helps to store the value in the next location
    if the desired location consists a value already.
    If the LIST is full. it uses negative index to store the value from start of the
    list.

"""

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] =(key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))


    def  __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element  in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


t= HashTable()

t['march 6'] = 400
t['march 4'] = 150
print(t.arr)
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
print(t.arr[9])
t['march 17'] = 450
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))

print(t.arr)
t.get_hash('march 17')
print(t['march 6'])
print(t['march 4'])

# array = [1,2,5,5,6,6,8]
#
# for ind, element in enumerate(array):
#     print(ind,':::',element)

del t['march 17']

print(t.arr)
print(t['march 17'])