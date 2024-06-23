import pandas as pd

df= pd.read_csv('nyc_weather.csv')

# print(df)
keys = []
for key in df['date']:
    keys.append(key)
# print(keys)

temp = []
for temps in df['temperature(F)']:
    temp.append(temps)
# print(temp)


class Hashing:
    def __int__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h+= ord(char)
        return h % self.Max

    def add_key(self, key, value):
        h= self.get_hash(key)
        found = False
        for ind, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][ind] = (key,value)
                found = True
                break

        if not found:
            self.arr.append((key,value))

    def get_items(self, key):
        h = self.get_hash(key)
        for ind, element in enumerate(self.arr(h)):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h =self.get_hash(key)
        for ind, element in enumerate(self.arr(h)):
            if element[0] == key:
                del self.arr[h][ind]

Ht = Hashing()

print(Ht.add_key(key,temp))
