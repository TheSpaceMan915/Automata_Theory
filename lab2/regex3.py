from string_helper import StringHelper
# три подряд пришедших символа 1


if __name__ == '__main__':
    helper = StringHelper(r"[01]*111[01]*")
    # number_words = int(input("Enter amount of words: "))

    helper.generate_words()
    helper.sort_strings()
    helper.match_strings()