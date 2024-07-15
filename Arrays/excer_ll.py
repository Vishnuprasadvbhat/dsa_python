class Node:
  def __init__(self, data= None, next = None) :
    self.data = data
    self.next = next 
  
class LinkedList:
  def __init__(self):
    self.head= None

   
  def insert_at_beginning(self, data):
    self.head = Node(data,None)
    return
    
  def insert_at_end(self,data):
    if self.head == None:
      self.insert_at_beginning(data)
    
    itr = self.head 

    while(itr.next):
      itr =itr.next 
    
    itr.next = Node(data, None)

  def get_length(self):
    count= 0
    itr =self.head

    while (itr):
      count += 1
      itr = itr.next

    return count


  def insert_at(self,index,data):
    if index<0 or index>self.get_length():
      raise Exception ("INVALID INDEX")
    
    if index ==0:
      self.insert_at_beginning(data)
    
    count = 0
    itr = self.head

    while itr:
      if count == index-1:
        node = Node(data,itr.next)
        itr.next = node 
        break 
      
      itr = itr.next 
      count +=1

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)

  def remove_at_index(self, index):
    if index<0 or index>self.get_length():
      raise Exception ('invalid')
    
    if index == 0:
      self.head = self.head.next
      return
    count = 0 
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next 
        break 
      itr = itr.next
      count += 1

  def insert_by_value(self,data_after, data):
    if self.head.data == None:
      self.insert_at_beginning(data)
    
    count = 0
    itr = self.head.data

    while(itr):
      if itr == data_after:
        node = Node(data,itr.next)
        break
      
      count += 1

  def remove_by_value(self, data):
    if self.head.data == None:
      print('LL is empty')

    count = 0

    itr = self.head
    while(itr.next):
      if itr.next.data == data:
        itr.next= itr.next.next
        break

      itr= itr.next





  def print(self):
    if self.head == None:
      print('LL is empty')
      return
    
    itr = self.head
    lst = ''
    while itr:
      lst += str(itr.data) + '-->'
      itr= itr.next
    print(lst)





if __name__ == '__main__':
  ll =LinkedList()
  ll.insert_at_beginning(54)
  ll.insert_at_end(10)
  ll.insert_at(1,15)
  # ll.print()
  # ll.remove_at_index(2)
  ll.print()
  # ll.insert_by_value(34,58)
  # ll.print()
  ll.remove_by_value(15)
  ll.print()