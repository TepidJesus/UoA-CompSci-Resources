
"""

This function takes a queue and a value. The function modifies the queue so the specified
value at the front of the queue. If the value is not in the queue then the queue is simply returned.

"""

### PASTE QUEUE CLASS HERE ###

def queue_jump(queue, value):
    if queue.size() == 0:
        return
    oth_queue = Queue()
    val = None
    if value == queue.peek():
        return 
    while not queue.is_empty():
        if queue.peek() == value and val == None:
            val = queue.dequeue()
        else:
            oth_queue.enqueue(queue.dequeue())

    if val != None:
        queue.enqueue(val)
    while oth_queue.size() > 0:
        queue.enqueue(oth_queue.dequeue())
