# assign5_5_2
"""
2.利用 reduce 函数求 0—100 之间奇数的和。
"""
from functools import reduce
print(reduce(lambda x,y:x+y,range(1,100,2)))
