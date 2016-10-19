num = [a for a in range(1, 101) if a % 7 != 0]
for x in num:
    print(str(x).ljust(6), end='')
    #print(format(str(x), '<6'), end='')
    if (num.index(x)+1) % 10 == 0:
        print() #默认结尾换行
