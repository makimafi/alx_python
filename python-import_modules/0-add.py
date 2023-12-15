#!/usr/bin/python3
from add_0 import add
if __name__=="__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2