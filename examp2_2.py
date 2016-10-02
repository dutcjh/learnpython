# -*- coding: utf-8 -*-
"""
例2-2：比较两个数的大小，数据由随机函数生成
"""
from random import randrange

def compareNum(num1,num2):
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1

num1, num2 = randrange(1,9), randrange(1,9)
print("num1 = %d" %num1,"num2 = %d" %num2, "result: %d" \
%compareNum(num1,num2),sep = '\n')
