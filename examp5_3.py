# -*- coding: utf-8 -*-
"""
例5.3 函数支持默认值
"""

def greet(name,greeting = 'Hello'):
    print(greeting,name+'!')
    
greet('Bob')
greet('Bob','Good morning')
greet(name='Tom')
greet(name='Tom',greeting='Good night')
