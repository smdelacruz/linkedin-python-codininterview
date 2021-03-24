# Input: A 2-dimensional array with integers.  Example below.
#[[-4, -3, -1, 1],
# [-2, -2,  1, 2],
# [-1,  1,  2, 3],
# [ 1,  2,  4, 5]]
# Returns:
#  The number of negative numbers in the array.
#  In the above case, this function should return 6
#  since there are 6 negative numbers in the array.
import time
# def count_negatives(given_array):
#     """
#     My solution for o(n^2)
#     """
#     start = time.time()
#     array_len = len(given_array)
#     counter = 0
#     for row in range(array_len):
#         for col in range(array_len):
#             if given_array[row][col] < 0:
#                 counter += 1
#     print(time.time() - start)
#     return counter


def count_negatives(given_array):
    """
    CS Dojo solution O(n)
    """
    count = 0
    row_i = 0
    col_i = len(given_array[0]) - 1
    while col_i >= 0 and row_i < len(given_array):
        print("coli", col_i)
        print("row_i", row_i)
        print("given_array[row_i][col_i]", given_array[row_i][col_i])
        if given_array[row_i][col_i] < 0:
            count += (col_i + 1)
            row_i += 1
        else:
            col_i -= 1
    return count



print(count_negatives([[-4, -3, -1, 1],
 [-2, -2, 1, 2],
 [-1,  1,  2, 3],
 [ 1,  2,  4, 5]]))