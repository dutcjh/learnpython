"""
2、从键盘输入华氏温度，要求输出摄氏温度。公式为：c=5/9*(F-32)
"""
f = input("Please input the Fahrenheit:")
try:
    f = float(f)    # 尝试将字符串转换成浮点数
except ValueError:
    print("The Fahrenheit should be a number!")
else:
    c = 5.0/9.0*(f-32)  # 求摄氏温度
    print("%.1f华氏温度 = %.1f摄氏温度" % (f, c))
