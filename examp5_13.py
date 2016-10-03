# -*- coding: utf-8 -*-
"""
例5.13 lambda函数的应用
"""

def func():
    x,y,m,n = 1,2,3,4
    add = lambda x,y:x+y
    print(add)
    sub = lambda m,n:m-n
    print(sub)
    return add(x,y)+sub(m,n)
    
print(func())