#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """indents a text"""
    e = "text_indentation() missing 1 required positional argument: 'text'"
    if text is None:
        raise TypeError(e)
    if type(text) is not str:
        raise TypeError("text must be a string")
    if not text:
        raise TypeError("Text is empty")
    c = 0
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            while c + 1 < len(text) and text[c + 1] == " ":
                c += 1
        c += 1
