class Gp:

  def __init__(self):
    self.graphs = {}
    

  def add_node(self,node):
    if node not in self.graphs:
      self.graphs[node] = []


  def add_edges(self,node,edge):

    if node in self.graphs:
      self.graphs[node].append(edge)

    else:
      raise KeyError(f'This {node} does not exists')
    
    
  
  def display(self):
    for nodes in self.graphs:
      print(f" Graph: {nodes} --->  {self.graphs[nodes]}")



if __name__ == "__main__":
  gg = Gp()

  gg.add_node('A')
  gg.add_node('B')
  gg.add_node('C')
  gg.add_node('D')

  gg.add_edges('A', 'B')
  gg.add_edges('A', 'C')
  gg.add_edges('B', 'E')
  gg.add_edges('C', 'E')
  gg.add_edges('D', 'A')

  gg.display()

