#!/usr/bin/python3
"""Module containing a Rectangle class that defines a rectangle"""


class Rectangle():
    """ defines a rectangle """

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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int)):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int)):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
