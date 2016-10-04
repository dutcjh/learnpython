# -*- coding: utf-8 -*-
"""
例5.22 用函数完善计算—编写求根的函数
"""
def findRoot(x,power,epsilon):
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0,x)
    high = max(1.0,x)
    ans = (high + low)/2.0
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

if __name__ == '__main__':
    print(findRoot(-0.125, 3, 0.001))
    print(findRoot(0.125, 3, 0.001))
    print(findRoot(16, 4, 0.001))
    print(findRoot(-27, 3, 0.001))