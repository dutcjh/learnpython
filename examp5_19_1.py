# -*- coding: utf-8 -*-
"""
例5-19_1：reduce()函数应用
"""
from functools import reduce

print(reduce(lambda x,y:x+y,range(0,100)))
print(reduce(lambda x,y:x*y,range(1,5+1)))