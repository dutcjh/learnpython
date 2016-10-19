def findDivisors(n1, n2):
    a = [1]
    for i in range(2,min(n1,n2)):
        if n1 % i == 0 and n2 % i == 0:
            a.append(i)
    return tuple(a)

print(findDivisors(1, 4))

