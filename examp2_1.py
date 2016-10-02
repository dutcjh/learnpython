# -*- coding: utf-8 -*-
"""
例2-1：类及对象命名举例
"""
class Student:
    __name = " "
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
        
if __name__ == "__main__":
    student = Student("borphi")
    print(student.getName())
