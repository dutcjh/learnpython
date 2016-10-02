# -*- coding: utf-8 -*-
"""
进制转换
"""

try:
    n = input("请输入一个整数: ")
    n = int(n)
except ValueError:
    print("输入错误！")
else:
    print("十进制整数 %d" %n)
    print("对应十六进制数：" + hex(n))
    print("对应八进制数：" + oct(n))
    print("对应二进制数：" + bin(n))
    