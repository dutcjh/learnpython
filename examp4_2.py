# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:39:47 2016

@author: ChenJianhui
"""

age = int(input('How old are you? '))
if age <= 2:
    print('free')
elif 2<age<13:
    print('child fare')
else:
    print('adult fare')
    