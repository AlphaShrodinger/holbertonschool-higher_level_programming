#!/usr/bin/python3
"""Define square by size based on 4-square.py file."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if one square has a greater area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square has a greater or equal area than the other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if one square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square has a smaller or equal area than the other."""
        return self.area() <= other.area()
