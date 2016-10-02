# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:36:16 2016

@author: ChenJianhui
"""

#def judge(num):
#    if num % 7 != 0:
#        return True
#p = lambda x: True if x%7 != 0 else False
print(list(filter(lambda x: True if x%7 != 0 else False,\
range(1,101))))
