"""
作业8.1 平面坐标处理的代码
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return other.getX() == self.x and other.getY() == self.y

    def __repr__(self):
        return 'Coordinate(%s, %s)' \
               % (str(self.getX()), str(self.getY()))


if __name__ == "__main__":
    point1 = Coordinate(1, 8)
    print(point1)  # str方法
    print(repr(point1))  # repr方法
    point2 = Coordinate(1, 8)
    print(point1 == point2)
