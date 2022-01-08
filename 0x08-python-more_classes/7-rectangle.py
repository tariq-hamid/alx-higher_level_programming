#!/usr/bin/python3
"""Module containing a Rectangle class that defines a rectangle"""


class Rectangle():
    """ defines a rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation Funtion

        Args:
            width: width of the rectangle, defaults to 0
            height: height of the rectangle, defaults to 0

        Returns:
            Nth
        """
        if not (isinstance(width, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not (isinstance(height, int)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Method that returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += print_symbol
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
