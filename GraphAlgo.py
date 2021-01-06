
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
                        q.get(g.graph[a])
                        q.put(a2)
            u.Info="red"





if __name__ == "__main__":
    t = DiGraph()
    t.add_node(1,0)
    t.add_node(2,0)
    t.add_node(3,0)
    t.add_node(4,0)
    t.add_edge(1,2,1)
    t.add_edge(1,4,8)
    t.add_edge(2,3,4)
    t.add_edge(4,3,3)

    g=GraphAlgo()
    g.Dijkstra(1,t)
    print(t.graph[3].tag)




    q = PriorityQueue()



   # while not q.empty():
       # print(q.get().tag)
       # q.task_done()
    #print(q.get().tag)
   # print(q.queue)



   # g.graph=t
    #g.load_from_json("b.txt")



