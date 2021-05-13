# Rif: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
"""
    Collegamenti:
    a -> c
    b -> c
    b -> e
    c -> a
    c -> b
    c -> d
    c -> e
    d -> c
    e -> c
    e -> b
"""
from collections import defaultdict


class GraphDictionary(object):

    graph = defaultdict(list)

    def addEdge(self, graph, u, v):
        graph[u].append(v)

    # definition of function
    def generate_edges(self, graph):
        edges = []
        # for each node in graph
        for node in graph:
            # for each neighbour node in a single node
            for neighbour in graph[node]:
                # if edge exists, append
                edges.append((node, neighbour))
        return edges


if __name__ == '__main__':
    g = GraphDictionary()

    # Creo la struttura del grafo
    graph = {"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
            }

    g.addEdge(graph, 'a', 'c')
    g.addEdge(graph, 'b', 'c')
    g.addEdge(graph, 'b', 'e')
    g.addEdge(graph, 'c', 'd')

    # Driver Function call
    # to print generated graph
    print(g.generate_edges(graph))