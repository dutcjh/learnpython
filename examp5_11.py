# -*- coding: utf-8 -*-
"""
例5.11 计算阶乘，递归函数， 
"""

def f(n):
    if n < 1: # 先测试
        return 1
    else: # 再调用递归式
        return n*f(n-1)
        
print(f(5))
