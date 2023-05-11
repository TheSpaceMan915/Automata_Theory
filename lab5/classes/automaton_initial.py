from lab5.classes.automaton_abstract import Automaton
from lab5.classes.vertex_s import VertexS
from lab5.classes.edge import Edge


class AutomatonInitial(Automaton):
    def __init__(self, number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes):
        super().__init__(number_vertexes, alphabet)
        self._list_starting_vertexes = list_starting_vertexes
        self._list_final_vertexes = list_final_vertexes

    def add_edges(self, edges):
        # adding connected edges to each vertex
        for edge in edges:
            vertex_from = edge.vertex_from
            self._list_lists_edges[vertex_from].append(edge)
            self._list_edges.append(edge)

    def check_type_vertex_s(self, vertex_s):
        for final_vertex in self._list_final_vertexes:
            if final_vertex in vertex_s.vertex_numbers:
                vertex_s.type = "final"
                return

        for starting_vertex in self._list_starting_vertexes:
            if starting_vertex in vertex_s.vertex_numbers:
                vertex_s.type = "starting"
                break

    def create_list_vertexes_s(self):
        # creating a list containing VertexS objects
        list_vertexes = [VertexS(i) for i in range(self._number_vertexes)]

        # going through each initial vertex and checking connected edges
        for i in range(self._number_vertexes):
            # adding an initial vertex (vertex_from) to the set
            vertex_s = list_vertexes[i]
            vertex_s.vertex_numbers.add(i)

            for edge in self._list_lists_edges[i]:
                if edge.state == "eps":
                    # adding another vertex (vertex_to) to the set
                    vertex_s.vertex_numbers.add(edge.vertex_to)
            self.check_type_vertex_s(vertex_s)

        return list_vertexes

    def create_list_lists_new_edges(self, list_vertexes_s):
        list_lists_edges = self._list_lists_edges
        list_lists_new_edges = [[] for _ in range(self._number_vertexes)]

        for vertex_s in list_vertexes_s:
            for symbol in self._alphabet:
                set_vertex_numbers = set()

                for number_vertex in vertex_s.vertex_numbers:
                    for edge in list_lists_edges[number_vertex]:
                        if edge.state == symbol:
                            set_vertex_numbers.add(edge.vertex_to)

                for s in list_vertexes_s:
                    if s.vertex_numbers.issubset(set_vertex_numbers):
                        new_edge = Edge(vertex_s.number, s.number, symbol)
                        list_lists_new_edges[vertex_s.number].append(new_edge)
        return list_lists_new_edges

    def check_str(self, string, alphabet):
        set_alphabet = set(alphabet)
        set_string = set(string)

        if set_string.issubset(set_alphabet):
            for char in string:
                for list in self._list_lists_edges:
                    for edge in list:
                        if edge.state == char:
                            AutomatonInitial.check_str(string[1:], alphabet)
                            if len(string) == 0:
                                print("Correct")
                            else:
                                print("Wrong")

        else:
            print("The string contains symbols that are from another alphabet. Enter another string")