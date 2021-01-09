import random

import matplotlib.pyplot as plt
import json
import numpy as np
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData
from queue import PriorityQueue
from queue import Queue
import sys
from collections import deque
class GraphAlgo(GraphAlgoInterface):
    list=[]
    stack = []
    def __init__(self):
        self.graph=DiGraph()
        self.visited=0

        self.Time=0
        self.lowlink=0
        self.components=[]
    def scc(self):
        n=len(self.graph.graph)

        self.time=0
        self.lowlink=np.zeros(len(self.graph.graph)+1)
        self.visited=np.zeros(len(self.graph.graph)+1)
        for u in self.graph.graph.keys():
            if(self.visited[u]==False):
                self.dfs(u)
        return self.components

    def dfs(self, u ):
        self.lowlink[u] = self.time=+1
        self.visited[u]=True
        self.stack.append(u)
        uIsComponentRoot=True

        for v in  self.graph.graph[u].neighbors.keys():
            if(self.visited[v]==False):
                self.dfs(v)
            if(self.lowlink[u]>self.lowlink[v]):
                self.lowlink[u]=self.lowlink[v]
                uIsComponentRoot=False
        if(uIsComponentRoot):
          component=[]
          while (1):
            x = self.stack.pop()
            component.append(x)
            self.lowlink[x] = sys.maxsize
            if (x == u):
                break



        self.components.append(component)

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

    def connected_components(self):
        st = []
        if self.graph.v_size() == 0:
            return self.list
        for temp in self.graph.get_all_values():
            if temp.disc == -1:
                self.SCC(temp, st)

        list_of_list = self.list
        self.nullify_scc()
        return list_of_list

    def SCC(self, u, stack):
        u.disc = self.Time
        u.low = self.Time
        self.Time += 1
        u.visited = True
        stack.append(u)

        for v in u.neighbors.keys():
            vert = self.graph.get_node(v)
            if vert.disc == -1:
                self.SCC(vert, stack)

                u.low = min(u.low, vert.low)
            elif vert.visited is True:
                u.low = min(u.low, vert.disc)

        w = -1  # To store stack extracted vertices
        if u.low == u.disc:
            l2 = []
            while w != u.key:
                node = stack.pop()
                l2.append(node)
                w = node.key
                node.visited = False

            self.list.append(l2)

    def nullify_scc(self):
        self.Time = 0
        self.list = []
        for runner in self.graph.get_all_values():
            runner.visited = False
            runner.disc = -1
            runner.low = -1

    def plot_graph(self) -> None:
        if self.graph is None:
            return
        x1=[]
        y1=[]

        for key in self.graph.graph.keys():

            geo=self.graph.graph[key].geo
            if geo is None:
                self.graph.graph[key].geo = (random.uniform(0.0, 70), random.uniform(0.0, 70), 0.0)
                geo = self.graph[key].geo

            x1.append(geo.x)
            y1.append(geo.y)

        plt.plot(x1, y1, '.', color='blue')
        for key in self.graph.graph.keys():
            if bool(self.graph.graph[key].neighbors)==False:
                plt.annotate(key,
                             xy=(self.graph.graph[key].geo.x, self.graph.graph[key].geo.y))
            for kei in self.graph.graph[key].neighbors.keys():
                plt.annotate(key, xy=(self.graph.graph[kei].geo.x, self.graph.graph[kei].geo.y), xycoords='data',
                             xytext=(self.graph.graph[key].geo.x, self.graph.graph[key].geo.y), textcoords='data',
                             arrowprops=dict(facecolor='g'))


        plt.legend(loc='upper left')
        plt.title("Graph")
        plt.show()

if __name__ == "__main__":
      g4 = DiGraph()
      for i in range(4):
        g4.add_node(i)
        g4.graph[i].geo=NodeData.Location()
        g4.graph[i].geo.x=random.uniform(0.0,4)
        g4.graph[i].geo.y = random.uniform(0.0, 3)

      g4.add_edge(0, 1, 0);
      g4.add_edge(2, 3, 0);
      g4.add_edge(1, 3, 0);



      g=GraphAlgo()
      g.graph=g4

      g.plot_graph()



    #for key in k:
        #for key2 in key:
            #print(key2.key,end=",")







   # while not q.empty():
       # print(q.get().tag)
       # q.task_done()
    #print(q.get().tag)
   # print(q.queue)



   # g.graph=t
    #g.load_from_json("b.txt")



