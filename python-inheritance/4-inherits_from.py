#!/usr/bin/python3
"""Inherits class"""


def inherits_from(obj, a_class):
    """If inherits same class, true, else false"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
