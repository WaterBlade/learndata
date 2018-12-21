from typing import List


class ExpNode:
    def __init__(self, el=None, left=None, right=None):
        self.el = el
        self.parent = self  # type: ExpNode
        self.left = left  # type: ExpNode
        self.right = right  # type: ExpNode

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


class ExpStr:
    def __init__(self, exp_str: str):
        self.expression = exp_str  # type: str
        self.idx = 0
        self.operand = ['+', '-', '*', '/', '(', ')']

    def move(self):
        self.idx += 1

    def current(self):
        if self.idx < len(self.expression):
            return self.expression[self.idx]
        else:
            return None

    def next_token(self):
        while self.current().isspace():
            self.move()

        t = self.current()
        self.move()
        while self.current() not in self.operand and not self.current().isspace():
            t += self.current()
            self.move()

        return t


def term(exp_str: ExpStr):
    token = exp_str.next_token()
    if token == '(':
        exp = expression(exp_str)
        if exp_str.next_token() == ')':
            return exp
        else:
            raise RuntimeError('Unmatched )')
    else:
        return ExpNode(token)


def uni_oper(exp_str: ExpStr):
    token = exp_str.next_token()
    if token == '-' or token == '+':
        return ExpNode(token, term(exp_str))
    else:
        return term(exp_str)


def bi_oper(exp_str: ExpStr):
    while exp_str.current().isspace():
        exp_str.move()

    left = uni_oper(exp_str)

    while exp_str.current().isspace():
        exp_str.move()

    oper = exp_str.current()
    exp_str.move()

    right = uni_oper(exp_str)

    return ExpNode(oper, left, right)


def expression(exp_str: ExpStr):
    exp = uni_oper(exp_str)

    while exp_str.current().isspace():
        exp_str.move()










class ExpTree:
    def __init__(self):
        self.root = None  # type: ExpNode
