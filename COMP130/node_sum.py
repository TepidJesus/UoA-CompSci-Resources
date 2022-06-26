
""" 

A function that sets nodes in a chain equal to the sum of the nodes before it.
e.g 2 --> 4 --> 6 becomes 2 --> 6 --> 12.

"""


def node_sum(node):
    current = node
    rolling_total = 0
    while current != None:
        rolling_total += current.data
        current.data = rolling_total
        current = current.next
    return node