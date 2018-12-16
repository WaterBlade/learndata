# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:50:08 2018

@author: Administrator
"""

def length(linked_node):
    if linked_node.next_ is None:
        return 1
    else:
        return length(linked_node.next_) + 1
    
def cal_sin(x, err):
    if x < err:
        return x - x**3 / 6
    else:
        return cal_sin(x/3, err)*(3-cal_tan(x/3, err)**2)/(1+cal_tan(x/3, err)**2)
    
    
def cal_tan(x, err):
    return cal_sin(x, err) / cal_cos(x, err)


def cal_cos(x, err):
    return 1 - cal_sin(x/2, err)


def convert_to_binary(x):
    if x == 1:
        return [1]
    else:
        return convert_to_binary(x // 2) + [x % 2]
    
    
def convert_to_binary2(x):
    ret = list()
    while x > 1:
        ret.append(x % 2)
        x = x // 2
    ret.append(1)
    ret.reverse()
    return ret


def fib_series(n):
    pass
    



if __name__ == '__main__':
    print(cal_sin(1, 1/18))
    print(convert_to_binary(150))
    print(convert_to_binary2(150))

