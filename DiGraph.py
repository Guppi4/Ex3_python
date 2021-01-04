
from NodeData import NodeData
from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

 def __init__(self):
    self.graph={}
    self.edgeSize=0
    self.mc=0


 def v_size(self):
   return len(self.graph)


 def e_size(self):
    return self.edgeSize

 def  get_all_v(self):
     return self.graph.values()

 def all_in_edges_of_node(self,id):
    t={}
    for key in self.graph.values():
         if(self.graph[key].getEdge(id)!=None):
             t0=self.graph[key].getEdge(id)
             t[key]=self.graph[key]
    return t






if __name__ == "__main__":
    t=DiGraph()
    t2=NodeData()
    t.graph[1]=t2
    t3=t.graph[1]
    print(t3.Info)

