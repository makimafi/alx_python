#!/usr/bin/python3
""" Module for Rectangle class """

from models.base import Base

class Rectangle(Base):
    """ Class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for width """
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for height """
        self.__height = value

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x """
        self.__x = value

    @property
    def y(self):
        """ Getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y """
        self.__y = value

Explanation:

    The Rectangle class inherits from the Base class.
    The constructor (__init__) calls the superclass (Base) constructor using super().__init__(id) to handle the id logic.
    Private instance attributes (__width, __height, __x, __y) are created along with their corresponding public getter and setter methods.
    The use of getters and setters allows for attribute validation and ensures that attributes are accessed and modified in a controlled manner.

The provided 1-main.py script can be used to test the functionality of the Rectangle class, as shown in the example output you provided.

