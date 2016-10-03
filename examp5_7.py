# -*- coding: utf-8 -*-
"""
例5.7 嵌套定义函数，内部函数直接引用外部变量
"""

def func():
    x,y,m,n = 1,2,3,4
    def add():
        return x+y
    def sub():
        return m-n
    return add()*sub()
    
print(func())

