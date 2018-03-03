from collections import defaultdict
class Graph:
    result = []
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def helper(self,v,visited):
 
        # Mark the current node as visited and print it
        visited[v]= True
        print('Node visited is', v)
        self.result.append(v)
        print('Visited Array after the visit', visited)
        print('Neighbors are', self.graph[v])
        
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[v]:
            
            if visited[neighbor] == False:
                
                print('I have not visited this node', neighbor)
                print('Let me explore its neighbors!')
                self.helper(neighbor, visited)
 
 
    def DFS(self,v):
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))
        
        print('Initial Visited Array ')
        print(visited)
        
        print('DFS started from', v)
        self.helper(v,visited)
        temp = self.result
        
        temp.remove(v)
        print(temp)
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
g.DFS(2)
