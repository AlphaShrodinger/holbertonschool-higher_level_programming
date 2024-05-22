#!/usr/bin/python3
"""Add atribute"""


def add_attribute(obj, name, value):
    """Assign attribute"""
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
