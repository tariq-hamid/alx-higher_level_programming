#!/usr/bin/python3
"""Square class to define a square"""


class Square:
    """Class to define a square"""

    def __init__(self, size=0, position=(0, 0)):
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
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], tuple) and isinstance(position[1], tuple) and
                position[0] >= 0 and position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter function to retrieve the value of __position

        Args:

        Returns:
            The value of __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function to set/change the value of __position

        Args:
            value: new value for __position

        Returns:
            Nth
        """
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method that returns the area of a square

        Args:

        Returns:
            Area of a square
        """
        return pow(self.__size, 2)

    def my_print(self):
        """Method that prints to stdout
        the square with the character #

        Args:

        Returns:
            Nth
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(" " * slef.__position[0], end='')
                print("#" * self.__size)
