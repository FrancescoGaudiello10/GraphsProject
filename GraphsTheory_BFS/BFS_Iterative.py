# Rif: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edge by node u and v
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print BFS of graph
    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)

        # Create a queue
        queue = []

        # Mark the source node as visited and start
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Main:
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
