from typing import List
from collections import deque


class KDTNode:
    def __init__(self, el=None, key=0, left=None, right=None):
        self.el = el
        self.parent = self  # type: KDTNode
        self.left = left  # type: KDTNode
        self.right = right  # type: KDTNode
        self.key = key  # type: int

    def __repr__(self):
        return self.el.__repr__()

    def append_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self
            # print('append %s to %s' % (node.el, self.el))
        # else:
            # print('append None to %s' % self.el)

    def append_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self
            # print('append %s to %s' % (node.el, self.el))
        # else:
            # print('append None to %s' % self.el)s


def preorder_print(node: KDTNode, cur_pre: str='', next_pre: str=''):
    print(cur_pre+str(node.el)+','+str(node.key))
    if node.left is not None and node.right is not None:
        preorder_print(node.left, next_pre+'|-', next_pre+'| ')
        preorder_print(node.right, next_pre + '|-', next_pre + '  ')
    elif node.right is not None:
        print(next_pre+'|-'+'*')
        preorder_print(node.right, next_pre + '|-', next_pre + '  ')
    elif node.left is not None:
        preorder_print(node.left, next_pre + '|-', next_pre + '| ')
        print(next_pre + '|-' + '*')


def find_largest_key(node: KDTNode, key: int)->KDTNode:
    largest = node
    stk = deque()
    stk.append(node)
    while len(stk) > 0:
        p = stk.popleft()

        if p.el[key] > largest.el[key]:
            largest = p

        if p.key != key and p.left is not None:
            stk.append(p.left)

        if p.right is not None:
            stk.append(p.right)

    return largest


def find_smallest_key(node: KDTNode, key: int)->KDTNode:
    smallest = node
    stk = deque()
    stk.append(node)
    while len(stk) > 0:
        p = stk.popleft()

        if p.el[key] < smallest.el[key]:
            smallest = p

        if p.key != key and p.right is not None:
            stk.append(p.right)

        if p.left is not None:
            stk.append(p.left)

    return smallest


class KDTree:
    def __init__(self, dimension: int):
        self.root = None  # type: KDTNode
        self.dimension = dimension

    def set_root(self, root: KDTNode):
        self.root = root
        root.parent = root

    def print_tree(self):
        if self.root is not None:
            print('*'*20)
            preorder_print(self.root)
            print('*' * 20)

    def insert(self, el: list):
        i = 0
        p = self.root
        prev = None
        while p is not None:
            prev = p
            if el[i] < p.el[i]:
                p = p.left
            else:
                p = p.right
            i = (i+1) % self.dimension

        newed = KDTNode(el, i)

        if self.root is None:
            self.root = newed
        elif el[(i-1) % self.dimension] < prev.el[(i-1) % self.dimension]:
            prev.append_left(newed)
        else:
            prev.append_right(newed)

    def search(self, ranges: List[List])->List[List]:
        ret = list()  # type: List[List]
        stk = deque()  # type: deque
        range_dimension = len(ranges)
        if self.root is not None:
            stk.append([self.root, 0])
        while len(stk) > 0:
            p, key = stk.popleft()

            if all(ranges[i][0] <= p.el[i] <= ranges[i][1] for i in range(range_dimension-1)):
                ret.append(p)

            if p.left is not None and ranges[key][0] <= p.el[key]:
                stk.append([p.left, (key+1) % self.dimension])

            if p.right is not None and p.el[key] <= ranges[key][1]:
                stk.append([p.right, (key+1) % self.dimension])

        return ret

    def delete(self, node: KDTNode):
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.left is not None:
            pre_node = find_largest_key(node.left, node.key)
            node.el, pre_node.el = pre_node.el, node.el
            self.delete(pre_node)
        else:
            post_node = find_smallest_key(node.right, node.key)
            node.el, post_node.el = post_node.el, node.el
            self.delete(post_node)

    def find_and_delete(self, el):
        p = self.root
        while p is not None:
            if p.el == el:
                break
            elif p.el[p.key] < el[p.key]:
                p = p.right
            else:
                p = p.left

        if p is not None:
            self.delete(p)


if __name__ == '__main__':
    tree = KDTree(3)
    tree.insert(['Kegan John', 1953, 80])
    tree.insert(['Adams Carl', 1977, 45])
    tree.insert(['Peterson Ian', 1969, 66])
    tree.insert(['Farrington Jill', 1988, 71])
    tree.insert(['Ruger Ann', 1979, 72])
    tree.insert(['Guyot Franz', 1979, 70])
    tree.insert(['Harel Alan', 1980, 70])
    tree.print_tree()

    tr2 = KDTree(2)
    tr2.insert([40, 60])
    tr2.insert([20, 80])
    tr2.insert([80, 40])
    tr2.insert([30, 60])
    tr2.insert([80, 20])
    tr2.insert([60, 80])
    tr2.insert([60, 20])
    tr2.insert([80, 90])
    tr2.print_tree()

    print(tr2.search([[50, 70], [10, 90]]))

    tr3 = KDTree(2)
    tr3.insert([50, 60])
    tr3.insert([40, 20])
    tr3.insert([30, 10])
    tr3.insert([20, 40])
    tr3.insert([10, 30])
    tr3.insert([20, 50])
    tr3.insert([10, 20])
    tr3.insert([40, 40])
    tr3.print_tree()
    tr3.find_and_delete([50, 60])
    tr3.print_tree()
    tr3.find_and_delete([20, 40])
    tr3.print_tree()
