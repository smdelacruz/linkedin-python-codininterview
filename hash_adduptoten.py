# Input: A list / array with integers.  For example:
# [3, 4, 1, 2, 9]
# Returns:
#  Nothing. However, this function will print out
#  a pair of numbers that adds up to 10. For example,
#  1, 9.  If no such pair is found, it should print
#  "There is no pair that adds up to 10.".

import time
# def pair10(given_list):
#     """
#     My solution O(n^2)
#     """
#     start = time.time()
#     for n in range(len(given_list)):
#         x = given_list[n]
#         counter = len(given_list) - 1
#         while counter != 0:
#             print("{} + {} = {}".format(x, given_list[counter], x + given_list[counter]))
#             if given_list.index(x) != counter and x + given_list[counter] == 10:
#                 print(time.time() - start)
#                 return x, given_list[counter]
#             else:
#                 counter -= 1
#     print(time.time() - start)
#     return "There is no pair that adds up to 10."


def pair10(given_list):
    """
    My solution O(n) after CS Dojo explain the logic
    """
    storage = {}
    for n in given_list:
        if 10 - n in storage:
            return n, 10-n
        else:
            storage[n] = 1
    return "There is no pair that adds up to 10."


# print(pair10([3, 4, 1, 2, 9]))
print(pair10([-11, -20, 2, 4, 30]))
print(pair10([1, 2, 9, 8]))
# print(pair10([1, 1, 1, 2, 3, 9]))
# print(pair10([1, 1, 1, 2, 3, 4, 5]))