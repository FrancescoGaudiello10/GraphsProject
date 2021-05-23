from collections import defaultdict

# Class to represent Graph
class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dizionario contenente la lista delle adiacenze
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtils(self, v, visited, stack):

        # Mark node current as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtils(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):

        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtils(i, visited, stack)

        # print reverse order
        print(stack[::-1])


# MAIN
if __name__ == '__main__':
    # Driver Code
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print("Following is a Topological Sort of the given graph:")

    # Function Call
    g.topologicalSort()


