from Lab5.classes.edge import Edge
from Lab5.classes.automaton_initial import AutomatonInitial
import re


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
    def print_vertexes_s(list_vertexes_s):
        print("Vertexes S:")
        print("{:<10} {:<15} {:<7}".format("Number", "Set vertexes", "Type"))
        for s in list_vertexes_s:
            print(s)
        print("")

    @staticmethod
    def print_data(number_vertexes, alphabet, starting_vertexes, final_vertexes):
        print("Initial data")
        print("number_vertexes:", number_vertexes)
        print("alphabet:", alphabet)
        print("starting_vertexes:", starting_vertexes)
        print("final_vertexes:", final_vertexes)
        print("")

    @staticmethod
    def create_tables(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes):
        lines = AutomatonHelper.read_file("../files/file2.txt")
        list_edges = AutomatonHelper.create_list_edges(lines)

        automaton_initial = AutomatonInitial(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes)
        automaton_initial.add_edges(list_edges)
        print("Table S")
        automaton_initial.print_edges()

        lines = AutomatonHelper.read_file("../files/file3.txt")
        list_edges = AutomatonHelper.create_list_edges(lines)

        automaton_initial = AutomatonInitial(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes)
        automaton_initial.add_edges(list_edges)
        print("Table P")
        automaton_initial.print_edges()

    @staticmethod
    def check_string(string, alphabet):
        set_alphabet = set(alphabet)
        set_string = set(string)

        if set_string.issubset(set_alphabet):
            pattern = r"(ab*)|(bb*abb*)"
            matcher = re.compile(pattern)
            print("Your string:", string)
            if matcher.search(string):
                print("Correct")
            else:
                print("Wrong")
        else:
            print("The string contains symbols that are from another alphabet. Enter another string")
