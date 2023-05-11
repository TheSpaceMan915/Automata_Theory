

class Vertex:
    def __init__(self, number):
        self._number = number
        self._vertex_numbers = set()
        self._type = None

    def add_vertex(self, vertex):
        self._vertex_numbers.add(vertex)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @number.deleter
    def number(self):
        del self._number

    @property
    def vertex_numbers(self):
        return self._vertex_numbers

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, vertex_type):
        self._type = vertex_type

    def __str__(self):
        return "{:<10} {:<15} {:<7}".format(self._number, str(self._vertex_numbers), self._type)
