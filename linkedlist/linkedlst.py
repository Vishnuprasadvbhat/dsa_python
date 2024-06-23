class Node:
  def __init__(self,data = None, next= None):
    self.data= data
    self.next = next

class linkedlist:
  def __init__(self):
    self.head = None

  def Insert_at_beginning(self,data):
    node = Node(data,self.head)
    self.head = node
  
  def print(self):
    if self.head is None:

      print('LL is empty')
      return

    itr= self.head
    lst = ''
    while itr:
      lst += str(itr.data) + '-->' if itr.next else str(itr.data)
      itr = itr.next 
    print(lst)

  def insert_at_end(self, data):
    if self.head is None:
      self.head= Node(data, None)
      return

    itr = self.head  # it traverses through the Linkedlist
    while itr.next: #untill there is a last element in the ll, i.e next
      itr = itr.next #Do itr = itr.next 

    #Once the itr (last node) is null
    #New node is attached to it, i.e insertion at the end
    itr.next = Node(data,None)
  
  def insert_values(self,data_list):
    self.head= None
    for data in data_list:
      self.insert_at_end(data)

  def length(self):
    count= 0
    itr = self.head
    while itr:
      count +=1
      itr = itr.next
    return count
  
  def remove_ele(self,index):
    if index<0 or index>=self.length() :
      raise Exception ('Invalid Index')
    
    if index == 0:
      self.head =self.head.next
      return
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next  = itr.next.next 
      
      itr= itr.next
      count += 1


  def insert_element(self, index, data):
    if index < 0 or index>self.length():
      raise Exception ('Invalid Index')
    
    if index == 0:
      self.Insert_at_beginning(data)
      return
    count = 0 
    itr = self.head
    while(itr):
      if count == index-1:
        node = Node(data,itr.next)
        itr.next = Node
        break
      itr = itr.next
      count += 1
      


if __name__ == '__main__':
  ll = linkedlist()
  ll.Insert_at_beginning(25)
  ll.Insert_at_beginning(20)
  ll.insert_at_end(79)
  # ll.insert_values(['Banana','Mango','Chikko'])
  # ll.remove_ele(20)
  print(ll.length())
  ll.insert_element(1, 25)
  ll.print()
