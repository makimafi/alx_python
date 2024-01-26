"""3-square.py - Module and Class Documentation

This module defines the `Square` class, which represents a square and
provides methods for managing and calculating properties of the square.

Classes:
    Square: A class representing a square with a private attribute 'size'.
"""

class Square:
    """Square class for representing a square.

    Attributes:
        __size (int): The size of the square. Private attribute.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with a given size.
        size (property): Getter method for retrieving the size of the square.
        size (setter): Setter method for setting the size of the square.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for retrieving the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
