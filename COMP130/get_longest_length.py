
"""

From a list of integers the function finds a return the length of longest consecutive sequence of non-zero values.

"""


def get_longest_length(values_list):
    longest_length = 0
    current_length = 0

    for i in range(len(values_list)):
        if values_list[i] == 0:
            current_length = 0
        else:
            current_length += 1
            if current_length > longest_length:
                longest_length = current_length
                
    return longest_length
