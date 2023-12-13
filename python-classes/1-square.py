#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size
        self.__validate_size()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.__validate_size()

    def area(self):
        return self.__size * self.__size

    def __validate_size(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

# Example usage:
try:
    square = Square(5)
    print(f"Square size: {square.size}")
    print(f"Square area: {square.area()}")

    square.size = 7
    print(f"Updated square size: {square.size}")
    print(f"Updated square area: {square.area()}")

    # Uncomment the line below to test the ValueError exception
    # square.size = -3

    # Uncomment the line below to test the TypeError exception
    # square.size = "not_an_integer"

except (TypeError, ValueError) as error:
    print(f"Error: {error}")
