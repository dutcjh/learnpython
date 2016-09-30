"""
1、从键盘输入一个整数，判断该数字能否被2和3同时整除，能否被2整除，
能否被3整除，不能被2和3整除。输出相应信息。
"""


def numjudge(num):  # 判断
    if num % 6 == 0:
        print("该数字能被2和3同时整除!")
    elif num % 3 == 0:
        print("该数字能被3整除!")
    elif num % 2 == 0:
        print("该数字能被2整除!")
    else:
        print("该数字不能被2和3整除!")


n = input("Please input a number:")
try:
    n = int(n)    # 尝试将字符串转换成正数
except ValueError:
    print("Should enter an integer number!")
else:
    numjudge(n)
