
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
     for key in self.graph[id1].neighbors.keys():
            t[key]=self.graph[id1].neighbors[key].w
     return t

 def get_mc(self):
     return self.mc

 def add_edge(self, id1,id2, weight):
    if((id1 in self.graph) and (id2 in self.graph )and ((id2 in self.graph[id1].neighbors)==(2<1)) and (id1!=id2)):
            self.graph[id1].createEdge(id1,id2,weight)
            self.mc+=1
            self.edgeSize+=1
            return 2>1

    return 2<1

 def get_all_values(self):
     return self.graph.values()

 def add_node(self, node_id,pos=0):
     if(node_id in self.graph):

         return (2<1)
     else:
        n=NodeData(node_id)
        n.geo=pos
        self.graph[node_id]=n
        self.mc+=1

        return  (2>1)

 def get_node(self, id1: int):
        if id1 not in self.graph:
            return None
        return self.graph[id1]
 def remove_node(self, node_id):
    if (node_id in self.graph):
        self.graph.pop(node_id)
        self.mc+=1
        for key in self.graph.keys():
            if((node_id in self.graph[key].neighbors)==(2>1)):
                self.graph[key].neighbors.pop(node_id)
                self.edgeSize-=1
                self.mc+=1
            return (2 > 1)

    else:
        return (2 < 1)

 def remove_edge(self, node_id1, node_id2):
     if (node_id1 in self.graph and node_id2 in self.graph ):
              if(node_id2 in self.graph[node_id1].neighbors):
                self.graph[node_id1].neighbors.pop(node_id2)
                self.edgeSize-=1
                self.mc+=1
                return (2>1)
              else:
                  return (2<1)
     else:
         return (2<1)





if __name__ == "__main__":
    t = DiGraph()
    t2 = NodeData(1, 7)
    t.graph[1] = t2
    t3 = NodeData(2, 99)
    t2.createEdge(1, 2, 9)
    t.graph[2] = t3
    t4 = NodeData(3, 4)
    t4.createEdge(3, 2, 8)
    t.graph[3] = t4
    #print(t.all_out_edges_of_node(1))
    #print(t.add_node())
    #print(t.add_edge(3,3,9))

    print(t.remove_edge(1,2))



