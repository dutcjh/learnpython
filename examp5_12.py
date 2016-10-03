# -*- coding: utf-8 -*-
"""
例5.11 计算Fibonacci数列的第n项，递归函数
"""

def fibo(n):
    if n == 1 or n == 2: # 先测试
        return 1
    else: # 再调用递归式
        return fibo(n-1)+fibo(n-2)
        
print(fibo(8))
