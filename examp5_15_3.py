# -*- coding: utf-8 -*-
"""
用迭代的方法求base^exp
"""

def iterPower(base,exp):
    p = 1;
    for x in range(0,exp):
        p *= base
    return p
        
print(iterPower(12,12))