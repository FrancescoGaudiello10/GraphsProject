# Rif: https://likegeeks.com/depth-first-search-in-python/
# Rappresento i grafi come dizionari chiave-valore
# 1. Implementing Depth First Search (non recursive)

graph = {
    "A": ["D", "C", "B"],
    "B": ["E"],
    "C": ["G", "F"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"]
}

graph_rec = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"]
}

def dfs_non_recursive(graph, source):

    if source is None or source not in graph:
        return "Invalid Input"

    path = []
    stack = [source]

    while len(stack) != 0:
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)


# 2. Implementing DFS using a recursive method
# E' possibile usare un approccio problem-solving utilizzando la ricorsione.
# Se il nodo è già visitato, torna indietro


def recursive_dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)

    return path


# 3. Depth First Search on a Binary Tree
# Un albero è uno speciale grafo dove i nodi hanno o due figli o nessuno.
# Una delle importanti proprietà dell'albero è che il figlio di sinistra è sempre minore o uguale del nodo padre
# mentre il figlio di destra a sua volta è sempre maggiore o uguale del nodo padre.



if __name__ == '__main__':
    print("Non Recursive:")
    DFS_Path = dfs_non_recursive(graph, "A")
    print(DFS_Path)
    print("**********************************")

    print("Recursive:")
    DFS_rec_Path = recursive_dfs(graph_rec, "A")
    print(" ".join(DFS_rec_Path))
    print("**********************************")


