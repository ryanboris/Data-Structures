# %%
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
# %%


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def enqueue(self, item):
        if self.size == 0:
            self.head = Node(item)
            self.last = self.head
        else:
            self.last.next = Node(item)
            self.last = self.last.next
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            removed = self.head.item
            self.head = self.head.next
            self.size -= 1
            return removed

    def len(self):
        return self.size
# %%
