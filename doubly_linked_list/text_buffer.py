from doubly_linked_list import DoublyLinkedList


class TextBuffer:
    # init gives us the option to initialize some text in the
    # buffer right off the bat
    def __init__(self, init=None):
        self.contents = DoublyLinkedList()
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        if init:
            init = init[::-1]
            i = 0
            while i < len(init):
                self.contents.add_to_head(init[i])
                i += 1

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        i = 0
        while i < len(string_to_add):
            self.contents.add_to_tail(string_to_add[i])
            i += 1

    def prepend(self, string_to_add):
        # reverse the incoming string to maintain correct
        # order when adding to the front of the text buffer
        string_to_add = string_to_add[::-1]
        i = 0
        while i < len(string_to_add):
            self.contents.add_to_head(string_to_add[i])
            i += 1

    def delete_front(self, chars_to_remove):
        i = 1
        while i <= chars_to_remove:
            self.contents.remove_from_head()
            i += 1

    def delete_back(self, chars_to_remove):
        i = chars_to_remove
        while i > 0:
            self.contents.remove_from_tail()
            i -= 1
    """
    Join other_buffer to self
    The input buffer gets concatenated to the end of this buffer
    The tail of the concatenated buffer will be the tail of the other buffer
    The head of the concatenated buffer will be the head of this buffer
    """

    def join(self, other_buffer):
        if isinstance(other_buffer, TextBuffer):
            other_buffer = other_buffer.__str__()
        self.join_string(other_buffer)

    def join_string(self, string_to_join):
        i = 0
        while i < len(string_to_join):
            self.contents.add_to_tail(string_to_join[i])
            i += 1


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
