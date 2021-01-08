
import json

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData
from queue import PriorityQueue
import sys
class GraphAlgo(GraphAlgoInterface):
    def __init__(self):
        self.graph=DiGraph()

    def save_to_json(self,file_name):
        graph={}
        nodes=[]
        edges=[]

        for key in self.graph.graph.keys():
            node={}
            pos1=str(self.graph.graph.get(key).geo().x)
            pos2 = str(self.graph.graph.get(key).geo().y)
            pos3 = str(self.graph.graph.get(key).geo().z)
            pos4=pos1+","+pos2+","+pos3
            node["pos"]=pos4
            node["id"]=key
            nodes.append(node)
            for key2 in self.graph.graph[key].neighbors.keys():
                edge={}
                edge["src"]=self.graph.graph[key].neighbors[key2].src
                edge["w"] = self.graph.graph[key].neighbors[key2].w
                edge["dest"] = self.graph.graph[key].neighbors[key2].dest
                edges.append(edge)

        graph["Edges"]=edges
        graph["Nodes"] =nodes

        try:
            with open(file_name, "w") as file:
               json.dump(graph,  fp=file)
        except IOError as e:
           print(e)

    def load_from_json(self, file_name):
        try:
            with open(file_name,"r") as file:
               d=json.load(file)
               g=DiGraph()
               temp={}
               nodes=d["Nodes"]
               edges=d["Edges"]

               for i in nodes:
                   n=NodeData(i["id"])
                   a={}
                   c=0;
                   for s in i["pos"].split(","):
                       a[c]=s
                       c+=1

                   n.setLocation(a[0],a[1],a[2])
                   g.add_node(n.key,n.geo)
               for j in edges:

                   g.add_edge(j["src"],j["dest"],j["w"])

               self.graph=g
               print(2>1)
        except IOError as e:
            print(e)
            return 0



    def Dijkstra(self,src,g):
        q=PriorityQueue()
        n=g.graph.get(src)
        for key in g.graph.keys():
            g.graph[key].tag=sys.maxsize
            g.graph[key].info="white"
            q.put(g.graph[key])
        n.tag=0
        while not q.empty():
            u=q.get()
            for a in u.neighbors.keys():
                a2=g.graph[a]
                if(g.graph[a].Info!="red"):
                    t=u.tag+g.graph[u.key].neighbors[a].w
                    if(g.graph.get(a).tag>t):
                        a2.tag=t
                        a2.pred=u.key
                        q.get(g.graph[a])
                        q.put(a2)
            u.Info="red"
    def  shortest_path(self, id1, id2):
         path=[]
         if(id1==id2):
             return float('inf'), path
         if ((id1  in self.graph.graph.keys())==False) or ((id2  in self.graph.graph.keys())==False):
             return float('inf'), path

         self.Dijkstra(id1, self.graph)
         if(self.graph.graph[id2].tag==sys.maxsize):
             for key in self.graph.graph.keys():
                 self.graph.graph[key].tag = sys.maxsize
                 self.graph.graph[key].info = "white"
             return float('inf'),path

         k=self.graph.graph[id2]
         path.insert(0,id2)
         w=0
         while k.key!=id1:
             k1=k.pred
             w = w + self.graph.graph[k1].neighbors[k.key].w
             k=self.graph.graph[k1]

             path.insert(0,k.key)
         return float(w),path













if __name__ == "__main__":
    t = DiGraph()
    t.add_node(1,0)
    t.add_node(2,0)
    t.add_node(3,0)
    t.add_node(4,0)
    t.add_node(5,0)
    t.add_edge(3,5,1)
    t.add_edge(1,2,2)
    t.add_edge(1,4,2)
    t.add_edge(2,3,4)
    t.add_edge(4,3,3)

    g=GraphAlgo()
    g.graph=t
    print(g.shortest_path(1,6))




    q = PriorityQueue()



   # while not q.empty():
       # print(q.get().tag)
       # q.task_done()
    #print(q.get().tag)
   # print(q.queue)



   # g.graph=t
    #g.load_from_json("b.txt")



