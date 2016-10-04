# -*- coding: utf-8 -*-
"""
例5-18：创建一个求圆面积、圆周长、
圆表面积和圆体积的模块。
"""
pi = 3.14159

def area(radius):
    return pi*(radius**2)
    
def circumference(radius):
    return 2*pi*radius
    
def sphereSurface(radius):
    return 4.0*area(radius)
    
def sphereVolume(radius):
    return (4.0/3.0)*pi*(radius**3)
