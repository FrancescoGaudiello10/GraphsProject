import networkx as nx

# DAG = Directed Acyclic Graph
dag = nx.digraph.DiGraph()

dag.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
dag.add_edges_from([('A', 'B'), ('A', 'E'), ('B', 'D'), ('E', 'C'),
                      ('D', 'G'),('C', 'G'),('C', 'I'), ('F', 'I')])


def dfs(dag, start, visited, stack):
    if start in visited:
        # node and all its branches have been visited
        return stack, visited

    if dag.out_degree(start) == 0:
        # if leaf node, push and backtrack
        stack.append(start)
        visited.append(start)
        return stack, visited

    # traverse all the branches
    for node in dag.neighbors(start):

        if node in visited:
            continue

        stack, visited = dfs(dag, node, visited, stack)

    # now, push the node if not already visited
    if start not in visited:
        print("pushing %s" % start)
        stack.append(start)
        visited.append(start)

    return stack, visited


def topological_sort_using_dfs(dag):

    visited = []
    stack = []
    start_nodes = [i for i in dag.nodes if dag.in_degree(i) == 0]

    for s in start_nodes:
        stack, visited = dfs(dag, s, visited, stack)

    print("Topological sorted:")

    while len(stack) != 0:
        print(stack.pop(), end=" ")


if __name__ == '__main__':
    topological_sort_using_dfs(dag)
    print("\n*****************")
    topological_sorting = nx.topological_sort(dag)
    for n in topological_sorting:
        print(n, end=" ")