# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:18:09 2016

@author: ChenJianhui
"""
try:
    total = 0
    s = '0'
    while s != 'done':
        num = int(s)
        total += num
        s = input('Enter a number (or "done"): ')
    print('\nThe sum is '+str(total))
except ValueError:
    print('\nError input!')
