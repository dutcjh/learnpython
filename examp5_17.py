# -*- coding: utf-8 -*-
"""
例5-17：创建模块，用于在屏幕上打印各种形状。
"""
import examp5_17_shapes

print(dir(examp5_17_shapes))

print(examp5_17_shapes.__doc__)
print()

print(examp5_17_shapes.CHAR)
print()

examp5_17_shapes.square(5)
print()

examp5_17_shapes.triangle(3)
print()

examp5_17_shapes.rectangle(3,8)
