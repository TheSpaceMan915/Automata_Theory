

class MinimizationHelper:
    def __init__(self, automaton):
        self._automaton = automaton
        self._list_equivalence_classes = [automaton.set_vertexes.difference(automaton.set_final_vertexes),
                                          automaton.set_final_vertexes.copy()]

    def create_equivalence_classes(self):
        vertex_subclass = set()
        list_vertex_subclasses = list()

        for vertex_class in self._list_equivalence_classes:
            for vertex in vertex_class:
                for state in self._automaton.alphabet:
                    for edge in self._automaton.list_lists_edges[vertex]:
                        if edge.state == state:
                            if edge.vertex_to not in vertex_class:
                                # adding the vertex to the subclass
                                vertex_subclass.add(vertex)

            if len(vertex_subclass) != 0:
                # adding a new vertex_subclass to the list of vertex_subclasses
                list_vertex_subclasses.append(vertex_subclass.copy())
                print("{} subclass of {}\n".format(vertex_subclass, vertex_class))

                # deleting vertexes that are in the subclass from the class
                vertex_class.difference_update(vertex_subclass)
                vertex_subclass.clear()

        # saving subclasses in the list of equivalence classes
        for subclass in list_vertex_subclasses:
            self._list_equivalence_classes.append(subclass)

    def get_minimized_edges(self):
        list_edges = list()
        for vertex_class in self._list_equivalence_classes:
            for vertex in vertex_class:
                for edge in self._automaton.list_lists_edges[vertex]:
                    if edge.vertex_to == edge.vertex_from:
                        if edge.vertex_from in vertex_class:
                            list_edges.append(edge)
                    else:
                        # adding to the list edges whose vertexes aren't in the vertex class
                        if edge.vertex_from not in vertex_class:
                            list_edges.append(edge)
                        elif edge.vertex_to not in vertex_class:
                            list_edges.append(edge)
        return list_edges

    def print_equivalence_classes(self):
        print("Equivalence classes:")
        for i in range(len(self._list_equivalence_classes)):
            print(self._list_equivalence_classes[i])
        print("")
