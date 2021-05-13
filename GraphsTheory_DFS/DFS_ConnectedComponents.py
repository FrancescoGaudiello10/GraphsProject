# RIF: https://likegeeks.com/depth-first-search-in-python/#The_Depth_First_Search_Algorithm
# Finding Connected components using DFS
# Le componenti connesse sono un altra proprietà dei grafi.
# Una componente connessa in un grafo non direzionale si riferisce a un set di nodi
# che è in grado di collegarsi con tutti gli altri vertici del percorso.

import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
graph.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

graph.add_edges_from([('A', 'B'), ('B', 'E'), ('A', 'E')])              # component 1
graph.add_edges_from([('C', 'D'), ('D', 'H'), ('H', 'F'), ('F', 'C')])  # component 2
graph.add_edge('G', 'I')                                                 # component 3

nx.draw(graph, with_labels=True, font_weight="bold")
# plt.show()

def find_connected_components(graph):
    visited = []
    connected_components = []

    for node in graph.nodes():
        if node not in visited:
            cc = []     # Connected component
            visited, cc = dfs_traversal(graph, node, visited, cc)
            connected_components.append(cc)
    return connected_components

def dfs_traversal(graph, start, visited, path):
    if start in visited:
        return visited, path

    visited.append(start)
    path.append(start)
    for node in graph.neighbors(start):
        visited, path = dfs_traversal(graph, node, visited, path)
    return visited, path


if __name__ == '__main__':
    connected_components = find_connected_components(graph)
    print("Total number of connected components = ", len(connected_components))
    for cc in connected_components:
        print(cc)

