from lab6.classes.abstract_automaton import Automaton


class BasicAutomaton(Automaton):
    def __init__(self, number_vertexes, alphabet, set_starting_vertexes, set_final_vertexes):
        super().__init__(number_vertexes, alphabet, set_starting_vertexes, set_final_vertexes)

    def add_edges(self, edges):
        # adding connected edges to each vertex
        for edge in edges:
            vertex_from = edge.vertex_from
            self._list_lists_edges[vertex_from].append(edge)
            self._list_edges.append(edge)

    def print_info(self):
        print("Automaton info:")
        print("number_vertexes:", self._number_vertexes)
        print("alphabet:", self._alphabet)
        print("starting_vertexes:", self._set_starting_vertexes)
        print("final_vertexes:", self._set_final_vertexes)
        print("")
