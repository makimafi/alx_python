# models/base.py

class Base:
    """
    This is the base class for managing id attributes in the project.
    It automatically assigns unique ids to instances.
    """

    # Private class attribute
    __nb_objects = 0

    # Class constructor
    def __init__(self, id=None):
        """
        Initialize the Base class.

        Parameters:
        - id (int): If provided, assign it to the public instance attribute id.
                   If not provided, generate a new id using __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects