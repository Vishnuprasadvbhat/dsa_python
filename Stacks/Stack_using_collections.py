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

    def show(self):
        if self.stack_size() == 0:
            return 'Stack Empty'
        else:
            return self.stacker


st = stack()
st.add_element(12)
st.add_element(22)
st.add_element(33)
print(st.stacker)
st.pop()
print(st.show())
