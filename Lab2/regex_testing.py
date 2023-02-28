# import re
# from string_helper import generate_string
# три символа 1 между двумя символами 0


# pattern = re.compile(r"[01]*0+1110+[01]*")
# list_str = []
# list_str_matched = []
# list_str_not_matched = []
#
# # generating words
# # amount_words = int(input("Enter amount of words: "))
# amount_words = 20
# for _ in range(amount_words):
#     list_str.append(generate_string())
#
# # sorting in ascending order
# list_str.sort()
# print("Sorted list:", list_str)
#
# for str in list_str:
#     res = pattern.search(str)
#     if res:
#         list_str_matched.append(str)
#     else:
#         list_str_not_matched.append(str)
# print("Matched:", list_str_matched)
# print("Not matched:", list_str_not_matched)