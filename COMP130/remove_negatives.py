
"""

Using a stack this function removes any negative values from the stack and returns them to the
stack in their origional order.

"""

### PASTE STACK CLASS HERE ###

def remove_negatives(stack):
    mid_stack = Stack()

    while not stack.is_empty():
        value = stack.pop()
        if value < 0:
            continue
        else:
            mid_stack.push(value)

    while not mid_stack.is_empty():
        stack.push(mid_stack.pop())
    
    return stack