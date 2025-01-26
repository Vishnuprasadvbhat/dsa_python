"""
Ways of representing a graph, In python we can use Tuple 
as the locations or two nodes are pairs we can represent 
it as (x,y) where x & y are two node in the graph

List of [ tuples(_) ]

"""


class Graph:

  def __init__(self):
    self.graphs = {}

  def add_data(self,start,end):
    if start not in self.graphs:
      self.graphs[start] = [end]
    
    else:
      self.graphs[start].append(end)
    
  def display(self):

    if not self.graphs:
      print("Graph is empty")
    
    else:
      for keys, value in self.graphs.items():
        print(f"Nodes in graph {keys} and edges are {value}")


if __name__ == "__main__":
  
  start = 'A'
  end = ['B', 'C']

  gp = Graph()

  for edges in end:
    graph = gp.add_data(start, edges)

  gp.display()