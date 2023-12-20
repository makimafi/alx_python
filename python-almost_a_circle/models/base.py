#!/usr/bin/python3
"""
Module: my_module
Description: This module contains the definition of the Base class.
"""

class Base:
    """
    Base class for object management.
    
    Attributes:
    - __nb_objects (int): A class variable to keep track of the number of objects created.
    - id (int): An instance variable representing the object's ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.
        
        Args:
        - id (int, optional): The ID to assign to the object. If not provided, a unique ID will be generated.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
