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
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
