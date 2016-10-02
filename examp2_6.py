# -*- coding: utf-8 -*-
"""
例2-6：根据美元不同硬币个数计算美分总额
"""

n = int(input('Nickels? '))
d = int(input('Dimes? '))
q = int(input('Quarters? '))

total = 5*n + 10*d + 25*q

print()
print(str(total)+"  cents")
