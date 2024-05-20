#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    line = ""

    for char in text:
        line += char
        if char in special_chars:
            print(line.strip())
            print()
            line = ""

    if line:
        print(line.strip())
