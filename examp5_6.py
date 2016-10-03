# -*- coding: utf-8 -*-
"""
例5.6 多个返回值的函数
"""
def sumDiff(x,y):
    SUM = x+y
    DIFF= x-y
    return SUM, DIFF
    
num1, num2 = eval(input("Please enter two number(num1,num2):"))
s,d = sumDiff(num1,num2)
print("The sum is", s, "and the difference is",d)
