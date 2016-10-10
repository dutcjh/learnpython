# calculator.py
"""
完成任意两个数的加(add)、减(sub)、乘(mult)、除(div)运算
"""
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b
    
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('ZeroDivisionError: division by zero')
