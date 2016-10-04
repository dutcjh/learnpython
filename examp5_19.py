# -*- coding: utf-8 -*-
"""
例5-19_1：filter()函数应用
"""
def func(x):
    if x>0:
        return True
        
print(filter(func,range(-9,10)))
print(list(filter(func,range(-9,10))))

print(list(filter(lambda x:True if x>0 else False,range(-9,10))))