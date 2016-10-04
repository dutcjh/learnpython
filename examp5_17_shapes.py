# -*- coding: utf-8 -*-
"""
例5-17：创建模块，用于在屏幕上打印各种形状。
"""

CHAR = '*'
def rectangle(height,width):
    for row in range(height):
        for col in range(width):
            print(CHAR,end = '')
        print()
def square(side):
    rectangle(side,side)
def triangle(height):
    for row in range(height):
        for col in range(1,row+2):
            print(CHAR,end='')
        print()
        