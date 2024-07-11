class Node:
  def __init__(self,data,next):
    self.data= data
    self.next = next


class linkedlist:
  def __init__(self) -> None:
    self.head = None


  def insert_begin(self,data):
    node =Node(data,self.head)
    self.head = node

# def insert(self,data):
#   if self.head == None:
#     self.insert_end(data)
#     return

#   itr = self.head

#   while itr:
#     itr =itr.next

#   itr = Node(data,itr.next)

  def insert_end(self,data):
    if self.head is None:
      self.head = Node(data,None)

    else:
      node = Node(data, None)

      itr = self.head

      while (itr.next):
        itr = itr.next

      itr.next = node


  def insert_values(self,data_List):
    self.head = None
    for data in data_List:
      self.insert_end(data)

  def remove_at_index(self,index):
    if index<0 and index<self.length():
       raise Exception('Invalid index')

    if index == 0:
      self.head = self.head.next

    count = 0
    itr = self.head
    while (itr):
      if count == index - 1:
        itr.next = itr.next.next
        break
      count += 1
      itr = itr.next

  def insert_at(self,index,data):
    if index<0 and index<self.length():
       raise Exception('Invalid index')

    if index == 0:
      self.head = self.head.next

    count = 0
    itr = self.head
    while (itr):
      if count == index - 1:
        node = Node(data,itr.next)
        itr.next = node
        break
      count += 1
      itr = itr.next

  def insert_after(self,data_after,data):
    if self.head == None:
      self.insert_begin(data)
      return
    
    if self.head.data == data_after:
      self.head.next = Node(data,self.head.next)
    itr = self.head

    while itr:
      if itr.data == data_after:
        itr.next = Node(data,itr.next)

      itr= itr.next

  def remove_by_values(self,data):
    if self.head.data == data:
      self.head = self.head.next

    itr = self.head
    while itr.next:
      if itr.next.data == data:
        itr.next = itr.next.next
      itr = itr.next

  def length(self):
    itr = self.head
    count  = 0
    while itr:
      count += 1
      itr = itr.next
    return print(count)


  def print(self):
    if self.head == None:
      print('LL is empty')
      return

    itr = self.head
    lst = ''
    while(itr):
      lst += str(itr.data) + '-->'
      itr = itr.next
    return print(lst)


ll = linkedlist()

ll.insert_begin(15)
ll.insert_begin(25)
ll.print()
ll.insert_end(255)
ll.insert_end(257)
ll.print()

data_list = [12,34,45,56,78]
ll.insert_values(data_list)
ll.length()
ll.print()
ll.remove_at_index(2)
ll.print()
ll.insert_at(2,65)
ll.print()
ll.insert_after(34,49)
ll.print()
ll.insert_after(49,152)
ll.print()
ll.remove_by_values(49)
ll.print()