# -*- coding: utf-8 -*-
"""
例5.10 全局变量的管理
"""

import examp5_10_gl

def add():
    examp5_10_gl._a = 3
    return "_a + _b=",examp5_10_gl._a+examp5_10_gl._b
def sub():
    examp5_10_gl._b = 4
    return "_a - _b=",examp5_10_gl._a-examp5_10_gl._b
    
print(add())
print(sub())

