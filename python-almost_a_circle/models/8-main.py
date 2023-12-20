#!/usr/bin/python3
def update(self, *args, **kwargs):
    """ Method to update attributes based on *args and **kwargs """
    if args:
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
    elif kwargs:
        for key, value in kwargs.items():
            setattr(self, key, value)
class Rectangle(Base):
    """ Class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Other methods and properties...

    def update(self, *args, **kwargs):
        """ Method to update attributes based on *args and **kwargs """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # Other methods and properties...

    def __str__(self):
        """ Method to override the default __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)