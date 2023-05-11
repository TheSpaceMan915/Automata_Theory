from abc import ABC


class Automaton(ABC):
    def __init__(self, number_vertexes, alphabet, set_starting_vertexes, set_final_vertexes,):
        self._number_vertexes = number_vertexes
        self._alphabet = alphabet
        self._list_edges = []
        self._list_lists_edges = [[] for i in range(number_vertexes)]
        self._set_vertexes = {i for i in range(number_vertexes)}
        self._set_starting_vertexes = set_starting_vertexes
        self._set_final_vertexes = set_final_vertexes

    @property
    def set_starting_vertexes(self):
        return self._set_starting_vertexes

    @property
    def set_final_vertexes(self):
        return self._set_final_vertexes

    @property
    def set_vertexes(self):
        return self._set_vertexes

    @property
    def list_lists_edges(self):
        return self._list_lists_edges

    @property
    def alphabet(self):
        return self._alphabet

    @set_starting_vertexes.setter
    def set_starting_vertexes(self, list_starting_vertexes):
        self._set_starting_vertexes = list_starting_vertexes

    @set_final_vertexes.setter
    def set_final_vertexes(self, list_final_vertexes):
        self._set_final_vertexes = list_final_vertexes

    def print_edges(self):
        print("Edges:")
        print("{:<5} {:<5} {:<7}".format("From", "To", "State"))
        for edge in self._list_edges:
            print(edge)
        print("")
