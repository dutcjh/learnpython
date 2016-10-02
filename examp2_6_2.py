# -*- coding: utf-8 -*-
"""
进制转换2
"""

try:
    n = input("请输入一个整数: ")
    if n[0] == '0':
        if (n[1] == 'x')|(n[1] == 'X'):
            b = 16
        elif (n[1] == 'o') | (n[1] == 'O'):
            b = 8
        else:
            b = 2
        a = n[2:]
    else:
        b = 10
        a = n
    a = int(a,b)
except ValueError:
    print("输入错误！")
else:
    if b != 10:
        print("%d进制数%s," %(b,n),"对应的十进制数为：%d" %a)
    else:
        print("十进制整数 %d" %a)
        print("对应十六进制数：" + hex(a))
        print("对应八进制数：" + oct(a))
        print("对应二进制数：" + bin(a))
