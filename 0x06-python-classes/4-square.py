#!/usr/bin/python3
"""Square class to define a square"""


class Square:
    """Class to define a square"""

    def __init__(self, size=0):
        """Instantiation function

        Args:
            size: size of the square

        Returns:
            Nth
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter function to retrieve the value of __size

        Args:

        Returns:
            The value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set/change the value of __size

        Args:
            value: new value for __size

        Returns:
            Nth
        """
        self.__size = value

    def area(self):
        """Method that returns the area of a square

        Args:

        Returns:
            Area of a square
        """
        return pow(self.__size, 2)
