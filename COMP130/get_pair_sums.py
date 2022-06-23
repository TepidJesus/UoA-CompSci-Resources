
"""

Returns a list of tuples containing the pairs of values from the numbers_list that add to a number greater
than the target_sum. Does not return any duplicates.

"""


def get_pair_sum_over(numbers_list, target_sum):
    numbers_list.sort()
    tuples_list = []

    for i in range(len(numbers_list)):

        for j in range(i + 1, len(numbers_list)):

            if numbers_list[i] + numbers_list[j] > target_sum:
                if (numbers_list[i], numbers_list[j]) not in tuples_list: # REMOVE THIS TO RETURN DUPLICATE PAIRS.
                    tuples_list.append((numbers_list[i], numbers_list[j]))

    return tuples_list