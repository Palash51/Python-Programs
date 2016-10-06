graph={0:[1,2],1:[2],2:[0,3],3:[3]}


def bfs(graph,start):
    visited=[]
    queue=[start]
    while(queue):
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            for vertices in graph[node]:
                queue.append(vertices)
        
    return visited        


start=3
print(bfs(graph,start))






'''
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


#def main():
g=Graph()
for i in range(6):
        g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(1,5,4)
g.addEdge(5,3,6)
g.addEdge(3,4,5)
for v in g:
    for w in v.getConnections():
        print v.getId(),",",w.getId(),",",v.getWeight(w)

#if __name__=="__main__":
 #   main()

'''
