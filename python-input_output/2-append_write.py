#!/usr/bin/python3
'''Append file'''


def append_write(filename="", text=""):
    '''File append method'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
