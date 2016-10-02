# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:15:26 2016

@author: ChenJianhui
"""

n = int(input('Enter an integer >= 0: '))
fact = 1
n2 = n
while n >= 1:
    fact *= n
    n -= 1

print(str(n2) + ' factorial is ' + str(fact))