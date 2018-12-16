from collections import deque
from logging import log
import math


def stack()->list:
    return list()


def queue()->deque:
    return deque()


class BSTNode:
    def __init__(self, el=None, left=None, right=None):
        self.el = el
        self.left = left  # type: BSTNode
        self.right = right  # type: BSTNode


ret = list()


def visit(node: BSTNode):
    ret.append(node.el)


def preorder(node: BSTNode):
    if node is not None:
        visit(node)
        preorder(node.left)
        preorder(node.right)


def inorder(node: BSTNode):
    if node is not None:
        inorder(node.left)
        visit(node)
        inorder(node.right)


def postorder(node: BSTNode):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        visit(node)


class BST:
    def __init__(self):
        self.root = None  # type: BSTNode

    def clear(self):
        pass

    def is_empty(self):
        return self.root is None

    def preorder(self):
        preorder(self.root)

    def inorder(self):
        inorder(self.root)

    def postorder(self):
        postorder(self.root)

    def search(self, el):
        p = self.root
        while p is not None:
            if el == p.el:
                return p
            elif el < p.el:
                p = p.left
            else:
                p = p.right

    def breadth_first(self):
        if self.root is not None:
            q = queue()
            q.append(self.root)
            while len(q) > 0:
                node = q.popleft()  # type: BSTNode
                visit(node)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

    def iterative_preorder(self):
        if self.root is not None:
            stk = stack()
            stk.append(self.root)
            while len(stk) > 0:
                p = stk.pop()  # type: BSTNode
                visit(p)
                if p.right is not None:
                    stk.append(p.right)
                if p.left is not None:
                    stk.append(p.left)

    def iterative_inorder(self):
        stk = stack()
        p = self.root  # type: BSTNode
        last_visit = p  # type: BSTNode
        while p is not None:
            if p.left is None and p.right is None:
                visit(p)
                last_visit = p
                p = stk.pop()
            elif p.left == last_visit:
                visit(p)
                last_visit = p
                if p.right is None:
                    if len(stk) == 0:
                        break
                    p = stk.pop()
                else:
                    stk.append(p)
                    p = p.right
            elif p.right == last_visit:
                last_visit = p
                if len(stk) == 0:
                    break
                p = stk.pop()
            else:
                stk.append(p)
                p = p.left

    def iterative_postorder(self):
        stk = stack()
        p = self.root  # type: BSTNode
        last_visit = p  # type: BSTNode
        while p is not None:
            if p.left is None and p.right is None:
                visit(p)
                last_visit = p
                if len(stk) == 0:
                    break
                p = stk.pop()
            elif p.left == last_visit:
                if p.right is None:
                    visit(p)
                    last_visit = p
                    if len(stk) == 0:
                        break
                    p = stk.pop()
                else:
                    stk.append(p)
                    p = p.right
            elif p.right == last_visit:
                visit(p)
                last_visit = p
                if len(stk) == 0:
                    break
                p = stk.pop()
            else:
                stk.append(p)
                p = p.left

    def morris_inorder(self):
        pass

    def insert(self, el):
        p = self.root  # type: BSTNode
        parent = p
        while p is not None:
            parent = p
            if el < p.el:
                p = p.left
            else:
                p = p.right

        if self.root is None:
            self.root = BSTNode(el)
        elif el < parent.el:
            parent.left = BSTNode(el)
        else:
            parent.right = BSTNode(el)

    def delete_by_merging(self, node: BSTNode):
        pass

    def find_and_delete_by_merging(self, el):
        p = self.root
        parent = p
        while p is not None:
            if p.el == el:
                break
            elif el < p.el:
                parent = p
                p = p.left
            else:
                parent = p
                p = p.right

        if p is not None:
            if p.left is None:
                if parent.left == p:
                    parent.left = p.right
                else:
                    parent.right = p.right
            elif p.right is None:
                if parent.left == p:
                    parent.left = p.left
                else:
                    parent.right = p.left
            else:
                max_in_left = p.left
                max_parent = p

                while max_in_left.right is not None:
                    max_parent = max_in_left
                    max_in_left = max_in_left.right

                if max_in_left.left is not None:
                    max_parent.right = max_in_left.left

                max_in_left.right = p.right
                if max_in_left != p.left:
                    max_in_left.left = p.left
                max_parent.right = None

                if parent.left == p:
                    parent.left = max_in_left
                else:
                    parent.right = max_in_left

    def delete_by_copying(self, node: BSTNode):
        pass

    def find_and_delete_by_copying(self, el):
        p = self.root
        parent = p
        while p is not None:
            if p.el == el:
                break
            elif el < p.el:
                parent = p
                p = p.left
            else:
                parent = p
                p = p.right

        if p is not None:
            if p.left is None:
                if parent.left == p:
                    parent.left = p.right
                else:
                    parent.right = p.right
            elif p.right is None:
                if parent.left == p:
                    parent.left = p.left
                else:
                    parent.right = p.left
            else:
                max_in_left = p.left
                max_parent = p

                while max_in_left.right is not None:
                    max_parent = max_in_left
                    max_in_left = max_in_left.right

                p.el = max_in_left.el

                if max_parent == p:
                    max_parent.left = max_in_left.left
                else:
                    max_parent.right = max_in_left.left

    def _rotate_right(self, grand, parent, child):
        if grand != self.root:
            if grand.left == parent:
                grand.left = child
            else:
                grand.right = child
        parent.left = child.right
        child.right = parent

    def _rotate_left(self, grand, parent, child):
        if grand != self.root:
            if grand.left == parent:
                grand.left = child
            else:
                grand.right = child
        parent.right = child.left
        child.left = parent

    def _create_backbone(self):
        p = self.root
        grand = p
        while p is not None:
            if p.left is not None:
                self._rotate_right(grand, p, p.left)
                p = p.left
            else:
                grand = p
                p = p.right

    def _create_perfect_tree(self):
        p = self.root

        n = 1
        while p is not None:
            p = p.right
            n += 1

        m = 2**(math.floor(math.log2(n+1))) - 1

        k = n - m
        grand = self.root
        parent = self.root
        child = parent.right
        while k > 0:
            self._rotate_left(grand, parent, child)


    def balance(self, el, left, right):
        pass


if __name__ == '__main__':
    tree = BST()
    tree.insert(50)

    tree.insert(25)

    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    tree.insert(40)
    tree.insert(35)
    tree.insert(45)

    tree.insert(75)

    tree.insert(60)
    tree.insert(55)
    tree.insert(65)

    tree.insert(90)
    tree.insert(85)
    tree.insert(95)

    print('breadth_first')
    ret.clear()
    tree.breadth_first()
    print(ret)

    print('preorder')
    ret.clear()
    tree.preorder()
    print(ret)

    ret.clear()
    tree.iterative_preorder()
    print(ret)

    print('inorder')
    ret.clear()
    tree.inorder()
    print(ret)

    ret.clear()
    tree.iterative_inorder()
    print(ret)

    print('postorder')
    ret.clear()
    tree.postorder()
    print(ret)

    ret.clear()
    tree.iterative_postorder()
    print(ret)

    print('delete by merging')
    tree.find_and_delete_by_merging(25)
    ret.clear()
    tree.inorder()
    print(ret)

    print('delete by copying')
    tree.find_and_delete_by_copying(75)
    ret.clear()
    tree.inorder()
    print(ret)

    print('create backbone')
    tree._create_backbone()
    ret.clear()
    tree.breadth_first()
    print(ret)
