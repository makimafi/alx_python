#!/usr/bin/python3
from models.base import base 

class base:
    private class attribut _nb_objects = 0
    class constructor: def __init__(self, id=None):

       def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
 