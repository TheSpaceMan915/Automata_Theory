

class Automaton:
    def __init__(self, number_vertexes, list_starting_vertexes, list_final_vertexes):
        self._number_vertexes = number_vertexes
        self._list_starting_vertexes = list_starting_vertexes
        self._list_final_vertexes = list_final_vertexes
        self._list_edges = []
        self._list_lists_edges = [[] for i in range(number_vertexes)]

    def add_edges(self, edges):
        # adding connected edges to each vertex
        for edge in edges:
            vertex_from = edge.get_vertex_from()
            self._list_lists_edges[vertex_from].append(edge)
            self._list_edges.append(edge)

    def print_edges(self):
        print("{:<5} {:<5} {:<7}".format("From", "To", "Symbol"))
        for edge in self._list_edges:
            print(edge)
