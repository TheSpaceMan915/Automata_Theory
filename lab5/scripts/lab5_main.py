from lab5.classes.automaton_initial import AutomatonInitial
from lab5.classes.automaton_non_deterministic import AutomatonNonDeterministic
from lab5.classes.automaton_helper import AutomatonHelper


# initialising data
number_vertexes = 4
alphabet = ["a", "b"]
list_starting_vertexes = [0, 1]
list_final_vertexes = [2]
AutomatonHelper.print_data(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes)

# reading a file containing edges
file_path = "../files/automaton_initial.txt"
lines = AutomatonHelper.read_file(file_path)
list_edges = AutomatonHelper.create_list_edges(lines)

# creating an initial automaton
automaton_initial = AutomatonInitial(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes)
automaton_initial.add_edges(list_edges)
print("Initial automaton")
automaton_initial.print_edges()

# creating s_vertexes (epsilon closures) and a deterministic automaton
vertexes_s = automaton_initial.create_list_vertexes_s()
AutomatonHelper.print_vertexes_s(vertexes_s)

# creating a deterministic automaton
automaton_non_deterministic = AutomatonNonDeterministic(number_vertexes, alphabet, vertexes_s)
AutomatonHelper.create_tables(number_vertexes, alphabet, list_starting_vertexes, list_final_vertexes)

# checking whether a string is acceptable or not
AutomatonHelper.check_string("abbocj", alphabet)
AutomatonHelper.check_string("b", alphabet)
AutomatonHelper.check_string("bab", alphabet)
