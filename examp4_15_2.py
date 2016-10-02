# -*- coding: utf-8 -*-
"""
二分法求解方根
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (low+high)/2.0
while (abs(ans**2 - x)) >= epsilon:
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to the square root of ' + str(x))
