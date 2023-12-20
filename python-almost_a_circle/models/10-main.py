@property
def size(self):
    """ Getter method for size """
    return self.width

@size.setter
def size(self, value):
    """ Setter method for size """
    self.width = value
    self.height = value
