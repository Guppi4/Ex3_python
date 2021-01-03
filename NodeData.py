
import sys
class NodeData():


    def __init__(self, k):
        self.key=k
        self.Info="white"
        self.dist=sys.maxsize
        self.tag =sys.maxsize
        self.weight=0
        self.neighbors={}

    def getEdge(self,dest):
        if(self.neighbors==None):
            return None
        return  self.neighbors.get(dest)
    def getNi(self):
        if(self.neighbors==None):
            return None
        return self.neighbors.values()
    def createEdge(self,dest,weight):
        edge=NodeData.EdgeData
        self.neighbors[dest]=edge

    class EdgeData():
        def __init__(self, src=0,dest=0,w=0):
            self.src=src
            self.dest=dest
            self.w=w
            self.info=""
            self.tag=-1


        ##def getWeight(self):









if __name__ == "__main__":
    t=NodeData(4)
    t1=NodeData.EdgeData(5,6)
    t.neighbors={1:t1,2:t1}
    print(len(t.neighbors))
    t.createEdge(5,6)
    print(t.neighbors)



