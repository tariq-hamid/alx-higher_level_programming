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
        if size < 0:
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the area of a square

        Args:

        Returns:
            Area of a square
        """
        return pow(self.__size, 2)

    def __lt__(self, s2):
        return self.area() < s2.area()

    def __gt__(self, s2):
        return self.area() > s2.area()

    def __eq__(self, s2):
        return self.area() == s2.area()

    def __le__(self, s2):
        return self.area() <= s2.area()

    def __ge__(self, s2):
        return self.area() >= s2.area()

    def __ne__(self, s2):
        return self.area() != s2.area()
