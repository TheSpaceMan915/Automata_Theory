from Lab5.classes.automaton_abstract import Automaton


class AutomatonNonDeterministic(Automaton):
    def __init__(self, number_vertexes, alphabet, list_vertexes_s):
        super().__init__(number_vertexes, alphabet)
        self._list_vertexes_s = list_vertexes_s
        # self.filter_vertexes(list_vertexes_s)

    # def filter_vertexes(self, list_vertexes_s):
    #     for vertex in list_vertexes_s:
    #         if vertex.type == "starting":
    #             self._list_starting_vertexes.append(vertex)
    #         elif vertex.type == "final":
    #             self._list_final_vertexes.append(vertex)


    def create_edges(self, list_old_edges,
                     list_initial_starting_vertexes, list_initial_final_vertexes):
        pass

    def check_type_vertexes_p(self):
        pass

    def create_list_vertexes_p(self):
        pass
