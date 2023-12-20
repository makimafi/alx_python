#!/usr/bin/python3
"""
Module: rectangle
Description: This module contains the definition of the Rectangle class.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
    - __width (int): Width of the rectangle.
    - __height (int): Height of the rectangle.
    - __x (int): x-coordinate of the rectangle.
    - __y (int): y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int, optional): x-coordinate of the rectangle (default is 0).
        - y (int, optional): y-coordinate of the rectangle (default is 0).
        - id (int, optional): The ID to assign to the object (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle instance.

        Returns:
        - int: The area value.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle instance with the character '#' to stdout,
        taking into account the x and y coordinates.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes based on their position in *args
        or using key/value pairs in **kwargs.

        Args:
        - *args: Variable number of positional arguments.
        - **kwargs: Variable number of keyword arguments (key/value pairs).
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
        - str: The string representation.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
