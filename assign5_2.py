# -*- coding: utf-8 -*-
"""
编写判断素数的函数。在主调函数中输出 1-100 之间的素数。
#def _odd_iter():
#    n = 1
#    while True:
#        n = n + 2
#        yield n
#def _not_divisible(n):
#    return lambda x: x % n > 0
#def primes():
#    yield 2
#    it = _odd_iter() 
#    while True:
#        n = next(it) 
#        yield n
#        it = filter(_not_divisible(n), it)
"""
from math import sqrt

def isPrimes(num):
    if num < 2:
        return False
    else:
        n = int(sqrt(num))+1
        for i in range(2, n):
            if num % i == 0:
                return False
        return True
        
print(list(filter(isPrimes, range(1, 101))))
