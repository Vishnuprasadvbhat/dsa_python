# Implementing Hashkey using ASCII values

'''This function returns the index value of the variable queried in form of string
It sums up the ASCII value of each string given as a  input and
returns its mod of size of the list '''
#
# def hash_fun(key):
#     h = 0
#     for char in key:
#         h += ord(char)
#     return h % 100 #assume 100 is the size of the list
#
# # print(ord('m'))
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def  __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None




t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 7'))
# print(t.get_hash('March 6'))
# t.add_value('march 6',500)
# t.add_value('March 6', 500)
print(t.arr)
# print(t.get('march 6'))
t['march 7'] = 500
t['march 6'] = 250
print(t.arr)
del t['march 6']
print(t.arr)




