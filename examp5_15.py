# -*- coding: utf-8 -*-
"""
例5.15 使用yield
"""

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        print(b)
        a, b = b, a+b
        n += 1
        
list(fab(12))
