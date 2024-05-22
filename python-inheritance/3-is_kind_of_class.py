#!/usr/bin/python3
"""Same class inhetitance"""


def is_kind_of_class(obj, a_class):
    """Returns true if isinstance, false if not"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
