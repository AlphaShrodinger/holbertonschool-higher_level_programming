#!/usr/bin/python3
"""define a Rectangle"""


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

    def area(self):
        """Rectangle area getter"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the Rectangle,
        or nothing if height/width are 0"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
