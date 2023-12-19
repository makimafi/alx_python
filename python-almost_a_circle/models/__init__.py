# models/base.py

class Base:
    # Private class attribute
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        # If id is provided, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # If id is not provided, generate a new id using __nb_objects
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects