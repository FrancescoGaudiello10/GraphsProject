# Rif: https://www.meccanismocomplesso.org/programming-graphs-in-python-part-1-grafi/
# In Python possiamo utilizzare i dizionari per rappresentare i grafi
# grazie al loro chiave-valore

# Dichiaro una classe
class Graph(object):

    # Inizializzo (costruttore): in questo modo il costruttore può essere richiamato anche senza argomento
    def __init__(self, graph=None):
        if graph == None:
            graph = {}
        self.__graph = graph

    # Esempio:
    # Graph() = in tal caso creerà un grafo vuoto senza nodi e archi utilizzando un dizionario come struttura dati
    # Se invece il costruttore verrà chiamato con:
    # Graph(graph)
    # allora verrà convertito in grafo il dizionario.

    # Aggiunta di un nodo:
    # Importante controllare che se un nodo non è presente!
    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []

    # Aggiunta di un edge (connessione tra due nodi)
    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph:
            self.__graph[node1].append(node2)
        else:
            self.__graph[node1] = [node2]

    # Ritorna la lista dei nodi esistenti
    def nodes(self):
        return list(self.__graph.keys())

    # Ritorna le connessioni (archi)
    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if(neighbour, node) not in edges:
                    edges.append((node, neighbour))
        return edges

    # Abbiamo bisogno di un metodo di "print" per stampare tutto
    def __str__(self):
        res = "Nodes: "
        for node in self.nodes():       # self.nodes() -> col self richiama il metodo di questa classe
            res += str(node) + " "
        res += "\nEdges: "
        for edge in self.edges():
            res += str(edge)
        return res

    # SECONDO STEP:
    # I PATH NEI GRAFI
    # Il calcolo dei path consiste nel determinare i percorsi possibili che si possono tracciare su un grafo partendo
    # da un nodo per raggiungerne un altro, sfruttando le connessioni presenti.
    # Il path di un grafo non orientato è la seguenza di nodi P = n1, n2, n3 ... np adiacenti tra loro
    # che definisce un possibile percorso da n1 a np.
    # Esso è valido quando il percorso non passa più di una volta sullo stesso nodo.

    # E' chiaro che è di interesse trovare il path più breve tra tutti.
    # Ad ogni ricorsione aggiunge via via un nodo a meno che il nodo non sia
    # il nodo di arrivo o uno già presente
    def find_path(self, start_node, end_node, path=None):
        if path == None:
            path = []
        graph = self.__graph
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node, end_node, path)
                if extended_path:
                    return extended_path
        return None

    # Implemento un metodo che trova TUTTI i path
    def find_all_path(self, start_vertex, end_vertex, path=[]):
        """ Trova tutti i possibili path dal vertice start fino a end """
        graph = self.__graph
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return []
        paths = []

        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_path(vertex, end_vertex, path)

                for p in extended_paths:
                    paths.append(p)
        return paths



if __name__ == '__main__':
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["A"],
        "D": ["B", "E"],
        "E": ["B", "D"]
    }

    g = Graph(graph)
    print(g)

    # Ora aggiungo un nodo
    g.add_node("F")

    # Il nodo sarà isolato
    print(g)

    # Creo la connessione tra il nodo C e F
    g.add_edge(("C", "F"))
    print(g)

    # Find path
    print("*** Find Path ***")
    g = Graph(graph)
    path = g.find_path("A", "E")
    print(path)

    # Find all Path
    print("*** Find all Path ***")
    g = Graph(graph)
    paths = g.find_all_path("A", "E")
    print(paths)

    # Per conoscere quale è il minimo path.
    print(min(paths, key=len))
