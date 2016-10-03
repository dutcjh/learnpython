# -*- coding: utf-8 -*-
"""
用递归的方法求base^exp
"""

def recurPower(base,exp):
    if exp == 0:
        return 1
    else:
        return base*recurPower(base,exp-1)
        
print(recurPower(12,12))