#!/usr/bin/python3
"""defines a Rectangle"""


class Rectangle:
    """A rectangle"""

    def __init__(self, width=0, height=0):
        """init for Rectangle"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
