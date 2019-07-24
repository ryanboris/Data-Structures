

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
# %%


import math


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        next_head = ListNode(value, None, self.head)
        if not self.head and not self.tail:
            self.head = next_head
            self.tail = next_head
            self.head.prev = None
            self.head.next = None
            self.length = 1
        else:
            self.head.prev = next_head
            next_head.prev = None
            self.head = next_head
            self.length += 1

    def remove_from_head(self):
        removed_head = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = self.head.next
            self.head.prev.delete()
            self.length -= 1
        return removed_head

    def add_to_tail(self, value):
        next_tail = ListNode(value, self.tail)
        if not self.head and not self.tail:
            self.head = next_tail
            self.tail = next_tail
            self.head.prev = None
            self.head.next = None
            self.length = 1
        else:
            self.tail.next = next_tail
            self.tail = next_tail
            self.length += 1

    def remove_from_tail(self):
        removed_tail = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.tail = self.head.prev
            self.tail.next.delete()
            self.length -= 1
        return removed_tail

    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.length -= 1

    def move_to_end(self, node):
        if self.length > 1 and node is not self.tail:
            self.tail.insert_after(node.value)
            self.tail = self.tail.next
        if node == self.head:
            self.head = node.next
        node.delete()

    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length = 0
        elif self.tail == node:
            self.remove_from_tail()
        elif self.head == node:
            self.remove_from_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1

    def get_max(self):
        max_val = -1 * math.inf
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val


# %%

class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            self.contents.add_to_head(init)
            self.contents.add_to_head(init)

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        self.contents.add_to_tail(string_to_add)

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct
        # order when adding to the front of the text buffer
        self.contents.add_to_head(string_to_add[::-1])

    def delete_front(self, chars_to_remove):
        pass

    def delete_back(self, chars_to_remove):
        pass

    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer
    The tail of the concatenated buffer will be the tail of the other buffer
    The head of the concatenated buffer will be the head of this buffer
    """

    def join(self, other_buffer):
        # we might want to check that other_buffer is indeed a text buffer
        # set self list tail's next node to be the head of the other buffer

        # set other_buffer head's prev node to be the tail of this buffer

        pass

    # if we get fed a string instead of a text buffer instance,
    # initialize a new text buffer with this string and then
    # call the join method
    def join_string(self, string_to_join):
        pass


if __name__ == '__main__':
    text = TextBuffer("Super")
    print(text)

    text.join_string("califragilisticexpealidocious")
    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey! ")
    print(text)

    text.delete_front(4)
    print(text)


# %%
