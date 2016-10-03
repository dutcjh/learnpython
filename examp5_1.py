# -*- coding: utf-8 -*-
"""
例5.1 求圆面积
"""

import math
def area(radius):
    return math.pi*radius**2
    
print(area(5.5))
print(2*(area(3)+area(4)))

