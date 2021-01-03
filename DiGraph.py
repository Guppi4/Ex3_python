

from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

 def __init__(self):
    self.graph={}
    self.edgeSize=0
    self.mc=0


 def v_size(self):
   return len(self.graph)


 def e_size(self) :
    print("ffff")



if __name__ == "__main__":
    t=GraphInterface()
    t.v_size()

