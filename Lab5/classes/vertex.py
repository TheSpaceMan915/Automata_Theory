

class Vertex:
    def __init__(self, name):
        self._name = name
        self._set_vertexes = set()

    def add_vertex(self, vertex):
        self._set_vertexes.add(vertex)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name

    def get_vertexes(self):
        return self._set_vertexes

    # test properties
    name = property(get_name,set_name,del_name)
    vertexes = property(get_vertexes)
