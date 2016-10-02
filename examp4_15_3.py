# -*- coding: utf-8 -*-
"""
牛顿-拉夫逊求解方根
"""

x = 25
epsilon = 1e-10
numGuesses = 0
ans = x/2.0
while (abs(ans**2 - x)) >= epsilon:
    numGuesses += 1
    ans = ans - (((ans**2)-x)/(2*ans))
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))
