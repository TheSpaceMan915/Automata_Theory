from lab7.classes.grammar_checker import GrammarChecker
from lab7.classes.grammar import Grammar


if __name__ == '__main__':
    # initialising the data
    n_rules = 3
    str_terminal_symbols = "cd"
    str_nonterminal_symbols = "ABS"
    list_left_parts = ["S", "B", "A"]
    list_right_parts = ["ccB", "cAd", "cd"]

    grammar = Grammar(n_rules, str_terminal_symbols,
                      str_nonterminal_symbols, list_left_parts,
                      list_right_parts)
    grammar.print_info()

    grammar_checker = GrammarChecker(grammar)
    grammar_checker.check_grammar()
