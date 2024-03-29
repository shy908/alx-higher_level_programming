#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file 
    (UTF8) and return the number of character written """

    n_characters = 0

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)

    n_characters = len(text)

    return n_characters
