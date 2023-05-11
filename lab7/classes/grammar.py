

class Grammar:
    eps = "e"

    def __init__(self, n_rules,
                 str_terminal_symbols, str_nonterminal_symbols,
                 list_left_parts, list_right_parts):
        self._n_rules = n_rules
        self._list_terminal_symbols = list(str_terminal_symbols)
        self._list_nonterminal_symbols = list(str_nonterminal_symbols)
        self._list_left_parts = list_left_parts
        self._list_right_parts = list_right_parts

    @property
    def n_rules(self):
        return self._n_rules

    @property
    def list_terminal_symbols(self):
        return self._list_terminal_symbols

    @property
    def list_nonterminal_symbols(self):
        return self._list_nonterminal_symbols

    @property
    def list_left_parts(self):
        return self._list_left_parts

    @property
    def list_right_parts(self):
        return self._list_right_parts

    def print_info(self):
        print("n_rules:", self._n_rules)
        print("terminal_symbols:", self._list_terminal_symbols)
        print("nonterminal_symbols:", self._list_nonterminal_symbols)
        print("left_parts:", self._list_left_parts)
        print("right_parts:", self._list_right_parts)
        print("")
