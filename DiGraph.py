
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
     return self.graph

 def all_in_edges_of_node(self,id):
    t={}
    for key in self.graph.keys():
         if(self.graph[key].getEdge(id)!=None):
             t[key] = self.graph[key].getEdge(id).w

    return t
 def all_out_edges_of_node(self, id1):
     t={}
     for key in self.graph[id1].neighbors:
            t[key]=self.graph[id1].neighbors[key].w
     return t











if __name__ == "__main__":
    t=DiGraph()
    t2=NodeData(1,7)
    t.graph[1]=t2
    t3 = NodeData(2,99)
    t2.createEdge(1,2,9)
    t.graph[2]=t3
    t4 = NodeData(3, 4)
    t4.createEdge(2, 1, 8)
    t.graph[3] = t4
    print(t.all_in_edges_of_node(1))
    #print(t.get_all_v())
    print(t.all_out_edges_of_node(1))


