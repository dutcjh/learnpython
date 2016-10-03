# -*- coding: utf-8 -*-
"""
例5.4 关键字参数
"""

def shop(where='store',what='pasta',howmuch='5 pounds'):
    print('I want you go to the', where)
    print('and buy',howmuch,'of',what+'.')

shop()
shop(what='sugar')
shop(howmuch='2 pounds',what='sugar')
shop(howmuch='2 pounds',what='sugar',where='super market')
