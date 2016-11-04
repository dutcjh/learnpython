"""
作业8.2 Person类
"""


class Person(object):
    """
    Class to represent a person.
    """
    def __init__(self):
        self.name = ''
        self.age = 0

    def display(self):
        print("Person (%s, %d)" % (self.name, self.age))

    def setAge(self, age):
        if 0 < age <= 150:
            self.age = age

    def getAge(self):
        return self.age

if __name__ == "__main__":
    p = Person()
    p.setAge(26)
    print(p.getAge())
    p.setAge(160)
    print(p.getAge())
    p.setAge(-1)
    print(p.getAge())
