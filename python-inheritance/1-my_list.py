#!/usr/bin/python3
"""Module to print a list"""


class MyList(list):
    """Prints a list"""

    def print_sorted(self):
        print(sorted(self))
