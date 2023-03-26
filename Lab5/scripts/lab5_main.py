from Lab5.classes.automaton import Automaton
from Lab5.classes.automaton_helper import AutomatonHelper


# initialising data
number_vertexes = 4
alphabet = ["a", "b"]
list_starting_vertexes = [0, 1]
list_final_vertexes = [2]
file_path = "../files/automaton_initial.txt"

# reading a file containing edges
lines = AutomatonHelper.read_file(file_path)
list_edges = AutomatonHelper.create_list_edges(lines)

# creating an initial Automaton
automaton_initial = Automaton(number_vertexes, list_starting_vertexes, list_final_vertexes)
automaton_initial.add_edges(list_edges)
print("Initial automaton")
automaton_initial.print_edges()
