# -*- coding: utf-8 -*-
"""
编写函数evalQuadratic(a, b, c, x)，
返回二项式a⋅x2+b⋅x+c的值。
"""


def evalQuadratic(a, b, c, x):
    return a*x*x+b*x+c

print(evalQuadratic(1,-2,1,4))