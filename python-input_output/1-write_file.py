#!/usr/bin/python3
'''Write file'''


def write_file(filename="", text=""):
    '''Write file method'''
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
