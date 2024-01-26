#!/usr/bin/python3
class Square:
    """
    Square class represents a square with a size attribute.

    Attributes:
        __size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

# Uncomment the following lines if you want to run the sample script
# my_square_1 = Square(3)
# print(type(my_square_1))
# print(my_square_1.__dict__)

# my_square_2 = Square()
# print(type(my_square_2))
# print(my_square
