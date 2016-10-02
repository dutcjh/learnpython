# -*- coding: utf-8 -*-
"""
蒙特卡罗法计算pi值
"""

from random import random
from math import sqrt
from time import clock

DARTS = int(input("Please input darts:"))
hits = 0
clock()
for i in range(1,DARTS):
    x,y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits += 1
pi = 4*(hits/DARTS)
print("pi的值是 %s" %pi)
print("程序运行时间是 %-5.5ss" %clock())


