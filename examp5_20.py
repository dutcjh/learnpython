# -*- coding: utf-8 -*-
"""
例5-20：map()函数应用
"""
print(list(map(lambda x:x**x,range(1,5))))
print(list(map(lambda x,y:x**y,range(1,6),\
range(6,1,-1))))