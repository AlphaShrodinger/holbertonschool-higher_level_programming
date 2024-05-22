#!/usr/bin/python3
"""My int"""


class MyInt(int):
    """Inherits integer"""

    def __eq__(self, other):
        """Return True if self and other not equal, else false"""
        return int(self) != other

    def __ne__(self, other):
        """Return True if self and other equal, else false"""
        return int(self) == other
