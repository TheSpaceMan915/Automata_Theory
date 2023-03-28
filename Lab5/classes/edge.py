

class Edge:
    def __init__(self, vertex_from, vertex_to, symbol):
        self._vertex_from = vertex_from
        self._vertex_to = vertex_to
        self._symbol = symbol

    @property
    def vertex_from(self):
        return self._vertex_from

    @property
    def vertex_to(self):
        return self._vertex_to

    @property
    def symbol(self):
        return self._symbol

    def __str__(self):
        return "{:<5} {:<5} {:<7}".format(self._vertex_from, self._vertex_to, self._symbol)

    # vertex_from = property(get_vertex_from)
    # vertex_to = property(get_vertex_to)
    # symbol = property(get_symbol)