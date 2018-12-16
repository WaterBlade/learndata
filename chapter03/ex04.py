# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:15:07 2018

@author: Administrator
"""


class Node:
    def __init__(self, el:int, _next=None):
        self.el = el
        self._next = _next #type: Node
        
    def insert_before(self, el):
        self._next = Node(self.el, self._next)
        self.el = el
        
    def insert_after(self, el):
        self._next = Node(el, self._next)
        
    def __repr__(self):
        return '%d' % self.el
        
        
class List:
    def __init__(self):
        self.head = None #type: Node
        self.tail = None #type: Node
        self.current = None #type: Node
        
    def clear(self):
        self.head = None
        self.tail = None
        
    def add(self, el:int):
        if self.head is None:
            self.head = Node(el)
            self.tail = self.head
            self.current = self.head
        else:
            self.tail._next = Node(el)
            self.tail = self.tail._next
            
    def at(self, index):
        i = 0
        cur = self.head
        while i < index:
            cur = cur._next
        return cur
    
    def append(self, lst):
        self.tail._next = lst.head
        
    def bubble_sort(self):
        if self.head != self.tail:
            changed = False
            while True:
                pre = self.head
                cur = self.head._next
                while cur is not None:
                    if pre.el > cur.el:
                        pre.el, cur.el = cur.el, pre.el
                        changed = True
                    pre, cur = cur, cur._next
                if changed == False:
                    return
                changed = False
                
    def get_middle(self):
        if self.head == self.tail:
            return self.head
        else:
            mid = self.head
            cur = self.head._next
            while cur._next is not None and cur._next._next is not None:
                cur = cur._next._next
                mid = mid._next
        return mid
            
    
    def nextItem(self)->int:
        if self.current != None:
            el = self.current.el
            if self.current._next != None:
                self.current = self.current._next
            else:
                self.current = None
            return el
        return None
    
    def equal(self, other)->bool:
        left = self.head
        right = other.head
        while left is not None and right is not None:
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left.el != right.el:
                return False
            else:
                left = left._next
                right = right._next
        return True
    
    def remove_at(self, index)->int:
        i = 0
        prev = cur = self.head
        while cur is not None:
            if i == index:
                ret = cur.el
                prev._next = cur._next
                return ret
            else:
                prev = cur
                cur = cur._next
                i += 1
        return None
    
    def remove_at_plural(self, index_list)->int:
        index_id = 0
        ret_list = list()
        i = 0
        prev = cur = self.head
        while cur is not None:
            if i == index_list[index_id]:
                ret_list.append(cur.el)
                prev._next = cur._next
                if index_id < len(index_list)-1:
                    index_id += 1
            else:
                prev = cur
                
            cur = cur._next
            i += 1
        return ret_list
    
    def reverse(self):
        if self.head != self.tail:
            self.tail = self.head
            pre = self.head
            cur = self.head._next
            while cur is not None:
                suf = cur._next
                cur._next = pre
                pre = cur
                cur = suf
            self.head = pre
            self.tail._next = None
        return self
            
    def convert_from_list(self, origin_list:list):
        for i in origin_list:
            self.add(i)
            
    def __repr__(self):
        ret = ''
        item = self.head #type: Node
        while item is not None:
            ret += '%d,'% item.el
            item = item._next
        return ret
    
    
class Iter:
    def __init__(self, lst: List):
        self.head = lst.head
        self.current = lst.head
        
    def value(self):
        if self.current is not None:
            return self.current.el
        else:
            return None
        
    def get(self):
        return self.current
        
    def forward(self, i:int):
        while i > 0 and self.current is not None:
            self.current = self.current._next
            i -= 1
        if i > 0:
            raise RuntimeError('Out of range!')
            
            
def merge(alist: List, blist: List):
    ret = List() #type: List
    a = alist.nextItem() #type: Node
    b = blist.nextItem() #type: Node
    while a is not None or b is not None:
        if a is None:
            ret.add(b)
            b = blist.nextItem()
        elif b is None:
            ret.add(a)
            a = alist.nextItem()
        else:
            if a <= b:
                ret.add(a)
                a = alist.nextItem()
            else:
                ret.add(b)
                b = blist.nextItem()
    return ret
    
    
if __name__ == '__main__':
    a = List()
    a.convert_from_list([1, 4, 7, 9, 10, 14, 25, 67, 89])
    print(a)
    b = List()
    b.convert_from_list([5, 6, 8, 11, 12, 21, 35, 40, 69, 90])
    print(b)
    c = merge(a, b)
    print(c)
    print(c.remove_at(100))
    print(c.remove_at(5))
    print(c)
    print(c.remove_at_plural([3, 5, 7, 9]))
    print(c)
    
    d = List()
    d.convert_from_list([1,2,3,4,5])
    
    e = List()
    e.convert_from_list([1,2,3,4,5])
    print(d.equal(e))
    print(c.equal(e))
    print(e.reverse())
    
    it = Iter(d)
    it.forward(3)
    it.get().insert_before(9)
    print(d)
    it.get().insert_after(100)
    print(d)
    
    print(c.get_middle())
    c.reverse()
    print(c)
    c.bubble_sort()
    print(c)
    
    
    
    
    
    