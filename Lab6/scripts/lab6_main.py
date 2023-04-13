from Lab6.classes.basic_automaton import BasicAutomaton
from Lab6.classes.minimization_helper import MinimizationHelper
from Lab6.classes.automaton_helper import AutomatonHelper
from pathlib import Path


if __name__ == '__main__':
    # initialising the data
    number_vertexes = 6
    alphabet = {"a", "b"}
    set_vertexes = {i for i in range(number_vertexes)}
    set_starting_vertexes = {0}
    set_final_vertexes = {3, 4, 5}

    # creating an initial automaton
    automaton = BasicAutomaton(number_vertexes, alphabet, set_starting_vertexes, set_final_vertexes)
    path = Path.cwd().parent.joinpath("files", "automaton.txt")
    lines = AutomatonHelper.read_file(path)
    list_edges = AutomatonHelper.create_list_edges(lines)
    automaton.add_edges(list_edges)
    automaton.print_info()
    automaton.print_edges()

    # creating equivalence classes
    minimization_helper = MinimizationHelper(automaton)
    minimization_helper.print_equivalence_classes()
    minimization_helper.create_equivalence_classes()
    minimization_helper.print_equivalence_classes()

    # minimizing the automaton
    minimized_automaton = BasicAutomaton(number_vertexes, alphabet,
                                         set_starting_vertexes, set_final_vertexes)
    list_minimized_edges = minimization_helper.get_minimized_edges()
    minimized_automaton.add_edges(list_minimized_edges)
    minimized_automaton.print_edges()
