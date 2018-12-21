class AVLNode:
    def __init__(self, el=None, left=None, right=None):
        self.el = el
        self.parent = self  # type: AVLNode
        self.left = left  # type: AVLNode
        self.right = right  # type: AVLNode
        self.balance_factor = 0  # type: int

    def append_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self
            print('append %d to %d' % (node.el, self.el))
        else:
            print('append None to %d' % self.el)

    def append_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self
            print('append %d to %d' % (node.el, self.el))
        else:
            print('append None to %d' % self.el)


def preorder_print(node: AVLNode, cur_pre: str='', next_pre: str=''):
    print(cur_pre+str(node.el)+','+str(node.balance_factor))
    if node.left is not None and node.right is not None:
        preorder_print(node.left, next_pre+'|-', next_pre+'| ')
        preorder_print(node.right, next_pre + '|-', next_pre + '  ')
    elif node.right is not None:
        print(next_pre+'|-'+'*')
        preorder_print(node.right, next_pre + '|-', next_pre + '  ')
    elif node.left is not None:
        preorder_print(node.left, next_pre + '|-', next_pre + '| ')
        print(next_pre + '|-' + '*')


class AVLTree:
    def __init__(self):
        self.root = None  # type: AVLNode

    def set_root(self, root: AVLNode):
        self.root = root
        root.parent = root

    def insert(self, el):
        p = self.root  # type: AVLNode
        parent = p
        while p is not None:
            parent = p
            if el < p.el:
                p = p.left
            else:
                p = p.right

        inserted = AVLNode(el)

        if self.root is None:
            self.root = inserted
        elif el < parent.el:
            parent.append_left(inserted)
        else:
            parent.append_right(inserted)

        self._update_balance_factor_for_insert(inserted)

    def find_and_delete_by_copying(self, el):
        p = self.root
        parent = p
        while p is not None:
            if p.el == el:
                break
            elif el < p.el:
                parent = p
                p = p.left
                print('%d unsatisfied, goto %d' % (parent.el, p.el))
            else:
                parent = p
                p = p.right
                print('%d unsatisfied, goto %d' % (parent.el, p.el))

        if p is not None:
            if p.left is None:
                print('%d left is None' % p.el)
                if parent.left == p:
                    print('%d stand by left' % p.el)
                    parent.append_left(p.right)
                    self._update_balance_factor_for_delete(parent)
                else:
                    print('p stand by right')
                    parent.append_right(p.right)
                    self._update_balance_factor_for_delete(parent, False)

            elif p.right is None:
                print('p right is not None')
                if parent.left == p:
                    print('p stand by left')
                    parent.append_left(p.left)
                    self._update_balance_factor_for_delete(parent)
                else:
                    print('p stand by right')
                    parent.append_right(p.left)
                    self._update_balance_factor_for_delete(parent, False)

            else:
                max_in_left = p.left
                max_parent = p

                while max_in_left.right is not None:
                    max_parent = max_in_left
                    max_in_left = max_in_left.right

                p.el = max_in_left.el

                if max_parent == p:
                    max_parent.append_left(max_in_left.left)
                    self._update_balance_factor_for_delete(max_parent)
                else:
                    max_parent.append_right(max_in_left.left)
                    self._update_balance_factor_for_delete(max_parent, False)

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
            self.set_root(child)
        parent.append_left(child.right)
        child.append_right(parent)

    def _rotate_left(self, grand: AVLNode, parent: AVLNode, child: AVLNode):
        if parent != self.root:
            if grand.left == parent:
                grand.append_left(child)
            else:
                grand.append_right(child)
        else:
            self.set_root(child)
        parent.append_right(child.left)
        child.append_left(parent)

    def _update_balance_factor_for_insert(self, inserted: AVLNode):
        q = inserted
        p = q.parent
        height_changed = True

        if p.left == q:
            p.balance_factor -= 1
            if p.right is not None:
                height_changed = False
        elif p.right == q:
            p.balance_factor += 1
            if p.left is not None:
                height_changed = False

        while p != self.root and height_changed:
            q = p
            p = q.parent

            if p.left == q:
                p.balance_factor -= 1
                if p.balance_factor == -2:
                    break
            elif p.right == q:
                p.balance_factor += 1
                if p.balance_factor == 2:
                    break

            if p.balance_factor == 0:
                height_changed = False

        if p.balance_factor == 2:
            if q.balance_factor == 1:
                self._insert_balance_rr(p, q)
            elif q.balance_factor == -1:
                self._insert_balance_rl(p, q)
        elif p.balance_factor == -2:
            if q.balance_factor == -1:
                self._insert_balance_ll(p, q)
            elif q.balance_factor == 1:
                self._insert_balance_lr(p, q)

    def _insert_balance_rr(self, par: AVLNode, child: AVLNode):
        self._rotate_left(par.parent, par, child)
        par.balance_factor = 0
        child.balance_factor = 0

    def _insert_balance_ll(self, par: AVLNode, child: AVLNode):
        self._rotate_right(par.parent, par, child)
        par.balance_factor = 0
        child.balance_factor = 0

    def _insert_balance_rl(self, par: AVLNode, child: AVLNode):
        left = child.left
        self._rotate_right(par, child, left)
        self._rotate_left(par.parent, par, left)
        par.balance_factor = -1
        child.balance_factor = 0
        left.balance_factor = 0

    def _insert_balance_lr(self, par: AVLNode, child: AVLNode):
        right = child.right
        self._rotate_left(par, child, right)
        self._rotate_right(par.parent, par, right)
        par.balance_factor = 1
        child.balance_factor = 0
        right.balance_factor = 0

    def _update_balance_factor_for_delete(self, del_par: AVLNode, left: bool=True):
        print('update balance %d' % del_par.el)
        p = del_par
        height_changed = True
        print('original balanced factor is % d' % p.balance_factor)
        if left:
            p.balance_factor += 1
            if p.right is not None:
                height_changed = False
        else:
            p.balance_factor -= 1
            if p.left is not None:
                height_changed = False
        print('updated balanced factor is % d' % p.balance_factor)
        print('height changed:', height_changed)

        while p != self.root and height_changed:
            q = p
            p = p.parent
            if p.left == q:
                p.balance_factor += 1
            elif p.right == q:
                p.balance_factor -= 1

            if p.balance_factor == -1 or p.balance_factor == 1:
                height_changed = False
            print('updated balanced factor for %d to % d' % (p.el, p.balance_factor))

        p = del_par
        if left:
            self._delete_balance_left(p)
        else:
            self._delete_balance_right(p)

        while p != self.root:
            q = p
            p = p.parent
            if p.balance_factor == 2 or p.balance_factor == -2:
                if q == p.left:
                    self._delete_balance_left(p)
                elif q == p.right:
                    self._delete_balance_right(p)

    def _delete_balance_left(self, par: AVLNode):
        print('In function delete balance left')
        print('parameter is %d' % par.el)
        right = par.right
        if right.balance_factor == 1:
            self._rotate_left(par.parent, par, right)
            par.balance_factor = 0
            right.balance_factor = 0
        elif right.balance_factor == 0:
            print('rotate %d through %d' % (right.el, par.el))
            print(right.left, right.right)
            print(par.left, par.right)
            self._rotate_left(par.parent, par, right)
            par.balance_factor = 1
            right.balance_factor = -1
            print(right.left, right.right)
            print(par.left, par.right)

        elif right.balance_factor == -1:
            left = par.right.left
            if left.balance_factor == -1:
                self._rotate_right(par, right, left)
                self._rotate_left(par.parent, par, left)
                par.balance_factor = 0
                right.balance_factor = 1
                left.balance_factor = 0
            elif left.balance_factor == 1:
                self._rotate_right(par, right, left)
                self._rotate_left(par.parent, par, left)
                par.balance_factor = -1
                right.balance_factor = 0
                left.balance_factor = 0

    def _delete_balance_right(self, par: AVLNode):
        left = par.left
        if left.balance_factor == 1:
            self._rotate_right(par.parent, par, left)
            par.balance_factor = 0
            left.balance_factor = 0
        elif left.balance_factor == 0:
            self._rotate_right(par.parent, par, left)
            par.balance_factor = 1
            left.balance_factor = -1
        elif left.balance_factor == -1:
            right = par.right.left
            if left.balance_factor == -1:
                self._rotate_right(par, left, right)
                self._rotate_left(par.parent, par, right)
                par.balance_factor = 0
                left.balance_factor = 1
                right.balance_factor = 0
            elif left.balance_factor == 1:
                self._rotate_right(par, left, right)
                self._rotate_left(par.parent, par, right)
                par.balance_factor = -1
                left.balance_factor = 0
                right.balance_factor = 0


if __name__ == '__main__':
    tree = AVLTree()
    tree.insert(5)
    tree.print_tree()
    print('*'*20)
    tree.insert(10)
    tree.print_tree()
    print('*' * 20)
    tree.insert(15)
    tree.print_tree()
    print('*' * 20)
    tree.insert(20)
    tree.print_tree()
    print('*' * 20)
    tree.insert(23)
    tree.print_tree()
    print('*' * 20)
    tree.insert(25)
    tree.print_tree()
    print('*' * 20)
    tree.insert(28)
    tree.print_tree()
    print('*' * 20)
    tree.insert(30)
    tree.print_tree()
    print('*' * 20)
    tree.insert(40)
    tree.print_tree()
    print('*' * 20)
    tree.find_and_delete_by_copying(23)
    tree.print_tree()
    print('*' * 20)
    tree.find_and_delete_by_copying(23)
    tree.print_tree()
    print('*' * 20)
