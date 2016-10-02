# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:26:02 2016

@author: ChenJianhui
"""

for row in range(1,10):
    for col in range(1,row+1):
        prod = row*col
        print('%dx%d=%-2d ' %(col,row,prod),end=' ')
    print("\n")

        