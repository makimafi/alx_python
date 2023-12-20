def display(self):
    """ Method to display the rectangle with '#' characters, considering x and y """
    for _ in range(self.__y):
        print()
    for _ in range(self.__height):
        print(" " * self.__x + "#" * self.__width)