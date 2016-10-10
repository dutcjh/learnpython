# assign5_5_1.py
"""
1.利用 filter 函数求0—100之间能被3 和5 同时整除的数。 
"""

print(list(filter(lambda x: True if (x % 3 == 0 and \
x % 5 == 0) else False, range(100))))
