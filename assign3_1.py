"""
1、从键盘输入圆半径r，输入圆柱高h，求圆周长、圆面积、圆球表面积、
圆球体积、圆1柱体积，并输出结果。
"""
from math import *
r = input("Input circle radius:")
try:
    r = float(r)    # 尝试将字符串转换成浮点数
except ValueError:
    print("The radius of the circle should be a positive number!")
else:   # 判断浮点数是否为负数
    assert r > 0, "The radius of the circle should be a positive number!"
    h = input("Input column height:")
    try:
        h = float(h)     # 尝试将字符串转换成浮点数
    except ValueError:
        print("The column height should be a positive number!")
    else:   # 判断浮点数是否为负数
        assert h > 0, "The column height should be a positive number!"
        circle = 2.0*pi*r   # 圆周长
        area = pi*r*r   # 圆面积
        area2 = 4.0*pi*r*r  # 圆球表面积
        volume = 4.0/3.0*pi*r**3    # 圆球体积
        volume2 = pi*r*r*h      # 圆柱体积
        print("圆半径:%.4f" % r, "圆柱高度:%.4f" % h, "圆周长:%.4f" % circle,
              "圆面积:%.4f" % area, "圆球表面积:%.4f" % area2,
              "圆球体积:%.4f" % volume, "圆柱体积:%.4f" % volume2, sep='\n')
