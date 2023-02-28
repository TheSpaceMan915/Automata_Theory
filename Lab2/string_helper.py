import random
import re


class StringHelper:
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)
        self.list_str = []
        self.list_str_matched = []
        self.list_str_not_matched = []

    def generate_string(self, length=8, alphabet="10"):
        return "".join(random.choice(alphabet) for _ in range(length))

    def generate_words(self, amount=20):
        for _ in range(amount):
            self.list_str.append(self.generate_string())

    # sorting in ascending order
    def sort_strings(self):
        self.list_str.sort()
        print("Sorted list:", self.list_str)

    def match_strings(self):
        for str in self.list_str:
            res = self.pattern.search(str)
            if res:
                self.list_str_matched.append(str)
            else:
                self.list_str_not_matched.append(str)
        print("Matched:", self.list_str_matched)
        print("Not matched:", self.list_str_not_matched)