from string_helper import StringHelper
# не более трех символов 0 между двумя символами 1


if __name__ == '__main__':
    helper = StringHelper(r"(1+01+)|(1+001+)|(1+0001+)")
    # number_words = int(input("Enter amount of words: "))

    helper.generate_words()
    helper.sort_strings()
    helper.match_strings()