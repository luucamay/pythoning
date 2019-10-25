from collections import defaultdict

# This class represents a directed graph 
# using adjacency list representation 
class Graph:

    # Constructor 
    def __init__(self):
        # default dictionary to store graph 
        self.graph = defaultdict(list)

    # function to add an edge to graph 
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Function to print a BFS of graph 
    def BFS(self, s):

        # Mark all the vertices as not visited 
        visited = defaultdict(bool) # set() can be used instead 

        # Create a queue for BFS 
        queue = []

        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0)
            print s,

            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def route_between_nodes(self, start, end):
        if start == end:
            return True
        queue = []
        visited = defaultdict(bool)
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            if  not start == None:
                for v in self.graph[start]:
                    if not visited[v]:
                        if v == end:
                            return True
                        visited[v] = True
                        queue.append(v)
        return False

# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph()
g.addEdge(0, 10)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 4)
g.addEdge(4, 4)
g.addEdge(11, 1)

g.BFS(2)
print ""
print g.route_between_nodes(2,1)
print g.route_between_nodes(2,10)
print g.route_between_nodes(2,11)