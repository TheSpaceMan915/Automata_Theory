from lab6.classes.edge import Edge


class AutomatonHelper:
    # the structure of the file (english symbols):
    # vertex_from vertex_to state
    @staticmethod
    def read_file(path):
        with open(path) as f:
            return f.readlines()

    @staticmethod
    def create_list_edges(list_strings):
        list_edges = []
        for string in list_strings:
            list_parameters = string.split()
            list_edges.append(Edge(int(list_parameters[0]), int(list_parameters[1]), list_parameters[2]))
        return list_edges
