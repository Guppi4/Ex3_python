from math import sqrt
import sys
from functools import cmp_to_key

class NodeData():

    def __lt__(self, other):
        return self.tag < other.tag


    def __init__(self,key=0, weight=0):
        self.key=key
        self.Info="white"
        self.dist=sys.maxsize
        self.tag =sys.maxsize
        self.weight=weight
        self.neighbors={}
        self. geo=NodeData.Location

    def getEdge(self,dest):
        if(self.neighbors==None):
            return None
        return  self.neighbors.get(dest)
    def getNi(self):
        if(self.neighbors==None):
            return None
        return self.neighbors.values()
    def createEdge(self,src,dest,weight):
        edge=NodeData.EdgeData(src,dest,weight)
        self.neighbors[dest]=edge

    def removeEdge(self,dest):
        return self.neighbors.pop(dest)
    def setLocation(self,p):
        loc = self.geo
        loc.x=p.x
        loc.y=p.y
        loc.z=p.z

    def setLocation(self, x, y,z):
        loc = self.geo
        loc.x=x
        loc.y=y
        loc.z=z

    class EdgeData():
        def __init__(self, src=0,dest=0,w=0):
            self.src=src
            self.dest=dest
            self.w=w
            self.info=""
            self.tag=-1


    class Location():

       def __init__(self):
          self.x=0.0
          self.y=0.0
          self.z=0.0

       def distance(self, g):
           dx=self.x-g.x
           dy=self.y-g.y
           dz=self.z-g.z
           t=(dx*dx+dy*dy+dz*dz)
           return sqrt(t)











if __name__ == "__main__":
    t=NodeData(4)
    t1=NodeData.EdgeData(5,6)
    t.neighbors={1:t1,2:t1}
    print(len(t.neighbors))
    t.createEdge(5,6)
    print(t.neighbors[2].src)



