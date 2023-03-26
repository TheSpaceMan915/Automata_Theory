from Lab5.classes.edge import Edge


class AutomatonHelper:
    # the structure of the file (english symbols):
    # vertex_from vertex_to symbol
    @staticmethod
    def read_file(path_relative):
        with open(path_relative) as f:
            return f.readlines()

    @staticmethod
    def create_list_edges(list_strings):
        list_edges = []
        for string in list_strings:
            list_parameters = string.split()
            list_edges.append(Edge(int(list_parameters[0]), int(list_parameters[1]), list_parameters[2]))
        return list_edges

    @staticmethod
    def create_list_s_vertexes(list_lists_edges):
        list_s_vertexes = []

        # creating n number of VertexS objects
        # going through each initial vertex and checking connected edges
        # if an edge has eps as its symbol, add the vertex_from and the vertex_to to a VertexS object
        # otherwise, add only vertex_from to a VertexS object
