#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        """Instantiation of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
