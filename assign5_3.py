# -*- coding: utf-8 -*-
"""
三、分别用迭代（gcdIter(a, b)）和递归（gcdRecur(a, b)）
方法编写函数求两个正整数的最大公约数。 
如： 
gcd(2, 12)=2 
gcd(6, 12)=6 
gcd(9, 12)=3 
gcd(17, 12)=1 
"""
# 辗转相除法迭代求最大公约数
def gcdIter(a, b): 
    if a < b:
        a,b = b,a
    r = a % b
    while r>0:
        a,b = b,r
        r = a % b
    return b

# 辗转相除法递归求最大公约数
def gcdRecur(a, b):
    if (a%b == 0):
        return b
    else:
        return gcdRecur(b, a%b)

print('迭代法求解结果：')
print('gcd(2, 12) =',gcdIter(2,12))
print('gcd(6, 12) =',gcdIter(6,12))
print('gcd(9, 12) =',gcdIter(9,12))
print('gcd(17, 12) =',gcdIter(17,12))
print('递归法求解结果：')
print('gcd(2, 12) =',gcdRecur(2,12))
print('gcd(6, 12) =',gcdRecur(6,12))
print('gcd(9, 12) =',gcdRecur(9,12))
print('gcd(17, 12) =',gcdRecur(17,12))
