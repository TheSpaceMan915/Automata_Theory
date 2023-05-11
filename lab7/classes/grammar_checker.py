

class GrammarChecker:
    def __init__(self, grammar):
        self._grammar = grammar

    def check_first_type_left_part(self):
        k = 0
        flag = False
        while k < len(self._grammar.list_left_parts):
            if len(self._grammar.list_left_parts[k]) <= len(self._grammar.list_right_parts[k]):
                k += 1
            else:
                print("the grammar does not satisfy the condition")
                break
        if k == (len(self._grammar.list_left_parts)):
            for elem in self._grammar.list_left_parts:
                for el in elem:
                    if (el in self._grammar.list_nonterminal_symbols) or (el in self._grammar.list_terminal_symbols):
                        flag = True
                    else:
                        flag = False
                        break
        else:
            print("the grammar is not context-sensitive")
            flag = False
        return flag

    def check_first_type_right_part(self):
        k = 0
        flag = False
        while k < len(self._grammar.list_right_parts):
            if len(self._grammar.list_left_parts[k]) <= len(self._grammar.list_right_parts[k]):
                k += 1
        if k == len(self._grammar.list_right_parts):
            for i in self._grammar.list_right_parts:
                for err in i:
                    if (err in self._grammar.list_nonterminal_symbols) or (err in self._grammar.list_terminal_symbols) or (i.isspace()):
                        flag = True
                    else:
                        break
        else:
            print("error")
        return flag

    def check_second_type(self):
        flag = False
        for elem in self._grammar.list_left_parts:
            if (len(elem) == 1) and (elem in self._grammar.list_nonterminal_symbols):
                flag = True
            else:
                break
        return flag

    def check_third_type_left_part(self):
        flag = False
        for i in self._grammar.list_left_parts:
            if (len(i) == 1) and (i in self._grammar.list_nonterminal_symbols):
                # print(i)
                flag = True
            else:
                break
        return flag

    def check_third_type_right_part(self):
        wN = 0
        Nw = 0
        ni = 0
        for i in self._grammar.list_right_parts:
            if (len(i) > 1) and (i[0] in self._grammar.list_terminal_symbols and i[-1] in self._grammar.list_nonterminal_symbols):
                wN += 1
            if (len(i) > 1) and (i[0] in self._grammar.list_nonterminal_symbols and i[-1] in self._grammar.list_terminal_symbols):
                Nw += 1
            if (len(i) == 1) and (i in self._grammar.list_terminal_symbols):
                ni += 1

        ptr = False
        if (wN > 0) and (Nw == 0) and (ni > 0):
            print("right linear grammar")
            ptr = True
        elif ((Nw > 0) and (wN == 0)) and (ni > 0):
            print("left linear grammar")
            ptr = True
        else:
            print("context-free grammar")
        return ptr

    def check_grammar(self):
        if self.check_third_type_left_part() and self.check_third_type_right_part():
            print("the 3rd type")
        elif self.check_second_type():
            print("the 2nd type")
        elif self.check_first_type_left_part() and self.check_first_type_right_part():
            print("the 1st type")
        else:
            print("0 type")
