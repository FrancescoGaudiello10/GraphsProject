# Rif: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
# 1.To generate the path from one node to the other node:
# Path of the graph
graph = {
    "a": ["c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["a", "d"],
    "e": ["b, c"],
}

def find_path(graph, start, end, path=[]):
    path = path+[start]
    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)

            if newpath:
                return newpath


print(find_path(graph, "d", "c"))
print("#########################")


# 2.Program to generate all te possible paths from one node to the other
def find_all_paths(graph, start, end, path=[]):
    path = path+[start]

    if start == end:
        return [path]

    paths=[]
    newpaths=[]
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)

        for newpath in newpaths:
            paths.append(newpath)
    return paths


print(find_all_paths(graph, "d", "c"))
print("#########################")


# 3. Program to generate the shortest path
# Rif: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

def find_shortest_path(graph, start, end, path=[]):
    path = path+[start]
    if start == end:
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


print(find_shortest_path(graph, "d", "c"))