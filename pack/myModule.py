# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:28:50 2016

@author: ChenJianhui
"""
def func():
    print("pack.myModule.func()")
    
if __name__ == '__main__':
    print('myModule 作为主程序运行')
else:
    print('myModule 被另一个模块调用')
