
import json

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from NodeData import NodeData


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
    g=GraphAlgo()
    g.graph=t
    g.save_to_json("file")



