class Node(object):
    """
    A node in an avl tree.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree(object):
    def __init__(self, node=None):

        self.node = node
        self.height = -1
        self.balance = 0

    def insert(self, key):
        node = Node(key)
        if not self.node:
            self.node = node
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        self.rebalance()

    def rebalance(self):
        self.update_height(recursive=False)
        self.update_balance(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.left_rotate()
                    self.update_height()
                    self.update_balance()
                self.right_rotate()
                self.update_height()
                self.update_balance()
            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.right_rotate()
                    self.update_height()
                    self.update_balance()
                self.left_rotate()
                self.update_height()
                self.update_balance()

    def update_height(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_height()
                if self.node.right:
                    self.node.right.update_height()

            self.height = 1 + max(self.node.left.height,
                                  self.node.right.height)
        else:
            self.height = -1

    def update_balance(self, recursive=True):
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balance()
                if self.node.right:
                    self.node.right.update_balance()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def right_rotate(self):
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def left_rotate(self):
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root
