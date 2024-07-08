"""
Write a function in python that can reverse a string using stack data structure.

reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

from collections import deque

class stack:
    def __init__(self):
        self.stacker = deque()

    def pop(self):
        if len(self.stacker) <= 0:
            return "stack empty"
        else:
            self.stacker.pop()

    def stack_size(self):
        return len(self.stacker)
    def add_element(self, val):
        self.stacker.append(val)
        return self.stacker

    def reverse_string(self,string):
        for i in string:
            self.add_element(i)

        s= ''
        s += self.pop()
        return s
    
    def show(self):
        if self.stack_size() == 0:
            return 'Stack Empty'
        else:
            return self.stacker


st= stack()
st.add_element(25)
print(st.show())
print(st.reverse_string('We will conquere COVID-19'))
print(st.show())