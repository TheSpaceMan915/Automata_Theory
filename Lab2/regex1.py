from string_helper import StringHelper
# три символа 1 между двумя символами 0


if __name__ == '__main__':
    helper = StringHelper(r"[01]*0+1110+[01]*")
    # number_words = int(input("Enter amount of words: "))

    helper.generate_words()
    helper.sort_strings()
    helper.match_strings()
