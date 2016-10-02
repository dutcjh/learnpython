# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:12:11 2016

@author: ChenJianhui
"""

n = int(input('Enter an integer >= 0: '))
fact = 1
for i in range(1,n+1):
    fact *= i
print(str(n) + ' factorial is ' + str(fact))
