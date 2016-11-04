"""
作业8.3 创建一个表示整数集合的新类
"""

class intSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        p = intSet()
        for e in self.vals:
            if e in other.vals:
                p.insert(e)
        return p

    def __len__(self):
        return len(self.vals)


if __name__ == '__main__':
    s1 = intSet()
    print('len(%s) = ' % s1 + str(len(s1)))
    s1.insert(1)
    s1.insert(2)
    s1.insert(3)
    print('len(%s) = ' % s1 + str(len(s1)))
