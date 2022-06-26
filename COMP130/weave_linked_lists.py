### THIS IS A METHOD SO SHOULD BE INCLUDED UNDER THE LINKEDLIST CLASS ###

"""

This method is passed one linked list and will interleave it with the current list in an alternating way.

"""

def weave_lists(self, other):
        current_slf = self.head
        current_oth = other.head
        if current_oth == None:
            return
        while current_oth != None:
            curr_nxt = current_slf.get_next()
            current_slf.set_next(current_oth)
            oth_nxt =  current_oth.get_next()
            current_oth.set_next(curr_nxt)
            current_oth = oth_nxt
            current_slf = curr_nxt