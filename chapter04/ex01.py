# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:45:33 2018

@author: Administrator
"""
from collections import deque


# exercise 01
def reverse_stack01(stack):
    s1 = list()
    s2 = list()
    while len(stack) > 0:
        s1.append(stack.pop())
    while len(s1) > 0:
        s2.append(s1.pop())
    while len(s2) > 0:
        stack.append(s2.pop())
        
        
def reverse_stack02(stack):
    s1 = deque()
    while len(stack) > 0:
        s1.append(stack.pop())
    while len(s1) > 0:
        stack.append(s1.popleft())
        

def reverse_stack03(stack):
    s1 = list()
    ith = 1
    limit = len(stack)
    while ith <= limit:
        top = stack.pop()
        while len(stack) > ith - 1:
            s1.append(stack.pop())
        stack.append(top)
        while len(s1) > 0:
            stack.append(s1.pop())
        ith += 1
        

# exercise 02
def sort_stack(stack):
    s1 = list()
    ith = 1
    limit = len(stack)
    while ith <= limit:
        top = stack.pop()
        while len(stack) > ith - 1:
            el = stack.pop()
            if top < el:
                el, top = top, el
            s1.append(el)
        stack.append(top)
        while len(s1) > 0:
            stack.append(s1.pop())
        ith += 1
        

# exercise 03      
def convert_stack01(stack):
    s1 = list()
    s2 = list()
    while len(stack) > 0:
        s1.append(stack.pop())
    while len(s1) > 0:
        s2.append(s1.pop())
    return s2


def convert_stack02(stack):
    s2 = list()
    ith = 1
    limit = len(stack)
    while ith <= limit:
        while len(stack) > 1:
            s2.append(stack.pop())
        top = stack.pop()
        while len(s2) > ith - 1:
            stack.append(s2.pop())
        s2.append(top)
        ith += 1
    return s2


# exercise 05
def sort_queue01(queue):
    q1 = deque()
    q2 = deque()
    while len(queue) > 0:
        top = queue.popleft()
        while len(queue) > 0:
            el = queue.popleft()
            if el < top:
                top, el = el, top
            q1.append(el)
        q2.append(top)
        while len(q1) > 0:
            queue.append(q1.popleft())
    
    while len(q2) > 0:
        queue.append(q2.popleft())


def sort_queue02(queue):
    q1 = deque()
    ith = 1
    limit = len(queue)
    while ith <= limit:
        top = queue.popleft()
        while len(queue) > ith-1:
            el = queue.popleft()
            if el < top:
                top, el = el, top
            q1.append(el)
        while len(queue) > 0:
            q1.append(queue.popleft())
        q1.append(top)
        while len(q1) > 0:
            queue.append(q1.popleft())
        ith += 1
            
        

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6]
    b = [6, 5, 4, 3, 2, 1]
    q = deque([6, 5, 4, 3, 2, 1])
    q2 = deque([4,5,63,7,2,9,1])
    print(a)
    reverse_stack01(a)
    print(a)
    reverse_stack02(a)
    print(a)
    reverse_stack03(a)
    print(a)
    sort_stack(b)
    print(b)
    c = convert_stack01(a)
    print(c)
    d = convert_stack02(c)
    print(d)
    sort_queue01(q)
    print(q)
    sort_queue02(q2)
    print(q2)
    
        