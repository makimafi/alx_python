#!/usr/bin/python3
class Square:
    def _init_(self, size=0):
        print("size, 89")
        class Square:
    def __init__(self, size):
        self.__size = size  # Private instance attribute

# Example usage:
# Create an instance of Square with a size of 5
square_instance = Square(5)

# Access the size attribute (though it's private, the name is _Square__size)
print(square_instance._Square__size)