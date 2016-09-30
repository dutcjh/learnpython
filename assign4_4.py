"""
2、打印出所有的“水仙花数”，所谓“水仙花数”是指一个3位数，
其各位数字立方和等于该数本身。
"""


def narcissi(num):  # 判断一个数是否为水仙花数
    if 99 < num < 1000:
        n1 = num // 100
        n2 = (num % 100) // 10
        n3 = num % 10
        if (n1**3 + n2**3 + n3**3) == num:
            return True

print(list(filter(narcissi, range(1000))))
