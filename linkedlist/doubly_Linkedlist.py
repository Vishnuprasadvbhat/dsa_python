class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data= data
        self.next = next

class Doubly_linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        if self.head == None:
            node = Node(None,data,self.head)
            self.head = node
        else:
            node = Node(None,data,self.head)
            self.head.prev = node
            self.head = node


    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(None,data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(itr,data, None)
        itr.next = node

    def get_lastnode(self):
        itr = self.head
        while itr.next:
            itr=itr.next
        return itr
    def print_backward(self):
        if self.head == None:
            print('LL empty')
            return

        last_node = self.get_lastnode()
        itr = last_node
        lls = ''
        while itr:
            lls +='<--' + str(itr.data)
            itr = itr.prev
        return print(lls)



    def print(self):
        if self.head == None:
            print('LL empty')
            return
        itr = self.head
        lls = ''
        while (itr):
            lls += str(itr.data) + '-->'
            itr = itr.next
        return print(lls)


ll = Doubly_linkedlist()

ll.insert_at_begin(25)
ll.print()
ll.insert_at_begin(28)
ll.insert_at_begin(29)
ll.print()
ll.insert_at_end(45)
ll.print()
ll.print_backward()
