#!/usr/bin/python3
"""
Module: square
Description: This module contains the definition of the Square class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
    - size (int): Size of the square.
    - x (int): x-coordinate of the square.
    - y (int): y-coordinate of the square.
    - id (int): The ID to assign to the object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): Size of the square.
        - x (int, optional): x-coordinate of the square (default is 0).
        - y (int, optional): y-coordinate of the square (default is 0).
        - id (int, optional): The ID to assign to the object (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        - str: The string representation.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
