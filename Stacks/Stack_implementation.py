class Stack:
    def __init__(self):
        self.top = -1
        self.size = 100
        self.stack = []

    def isfull(self):
        return True if self.top == self.size-1  else False

    def isempty(self):
        return True if self.top == -1 else False

    def push(self, value):
        if self.isfull():
            return print("Stack is full")

        self.top += 1
        self.stack.append(value)

    def pop(self,value):
        if self.isempty():
            return print('StacK is empty')

        self.top -= 1
        self.stack.pop()

    def peek(self):
        if self.isempty():
            return False

        else:
            return print(self.stack[self.top])
    def show(self):
        if self.isempty():
            return print('Stack underflow')
        else:
            return print(self.stack)


stack = Stack()

stack.push(20)
stack.push(10)
stack.push(60)
stack.isfull()
stack.isempty()
stack.peek()
stack.show()





