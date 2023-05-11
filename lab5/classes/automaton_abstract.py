from abc import ABC


class Automaton(ABC):
    def __init__(self, number_vertexes, alphabet):
        self._number_vertexes = number_vertexes
        self._alphabet = alphabet
        self._list_edges = []
        self._list_lists_edges = [[] for i in range(number_vertexes)]

    def print_edges(self):
        # print("Edges:")
        print("{:<5} {:<5} {:<7}".format("From", "To", "Symbol"))
        for edge in self._list_edges:
            print(edge)
        print("")

    @property
    def list_starting_vertexes(self):
        return self._list_starting_vertexes

    @property
    def list_final_vertexes(self):
        return self._list_final_vertexes

    @list_starting_vertexes.setter
    def list_starting_vertexes(self, list_starting_vertexes):
        self._list_starting_vertexes = list_starting_vertexes

    @list_final_vertexes.setter
    def list_final_vertexes(self, list_final_vertexes):
        self._list_final_vertexes = list_final_vertexes

    @property
    def list_lists_edges(self):
        return self._list_lists_edges
