import math


class AVLNode:
    def __init__(self, el=None, parent=None, left=None, right=None):
        self.el = el
        self.parent = parent  # type: AVLNode
        self.left = left  # type: AVLNode
        self.right = right  # type: AVLNode
        self.balance_factor = 0  # type: int

    def append_left(self, node):
        self.left = node
        node.parent = self

    def append_right(self, node):
        self.right = node
        node.parent = self


def preorder_print(node: AVLNode, cur_pre: str='', next_pre: str=''):
    if node is not None:
        print(cur_pre+str(node.el))
        preorder_print(node.left, next_pre+'|-', next_pre+'| ')
        preorder_print(node.right, next_pre+'|-', next_pre+'  ')


class AVLTree:
    def __init__(self):
        self.root = None  # type: AVLNode

    def insert(self, el):
        pass

    def print_tree(self):
        if self.root is not None:
            preorder_print(self.root)

    def _rotate_right(self, grand: AVLNode, parent: AVLNode, child: AVLNode):
        if parent != self.root:
            if grand.left == parent:
                grand.append_left(child)
            else:
                grand.append_right(child)
        else:
            self.root = child
        parent.append_left(child.right)
        child.append_right(parent)

    def _rotate_left(self, grand: AVLNode, parent: AVLNode, child: AVLNode):
        if parent != self.root:
            if grand.left == parent:
                grand.append_left(child)
            else:
                grand.append_right(child)
        else:
            self.root = child
        parent.append_right(child.left)
        child.append_left(parent)

    def _update_balance_factor(self, start: AVLNode):
        q = start
        p = q.parent

        if p.left == q:
            p.balance_factor -= 1
        else:
            p.balance_factor += 1

        while p != self.root and p.balance_factor != 2 and p.balance_factor != -2:
            q = p
            p = q.parent
            if q.balance_factor == 0:
                break
            if p.left == q:
                p.balance_factor -= 1
            else:
                p.balance_factor += 1

# Unfinished


