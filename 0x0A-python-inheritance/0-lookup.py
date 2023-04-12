#!/usr/bin/python3
"""
=============================
Module with the method lookpu
=============================
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods
    of an object.
    Parameters:
        obj: Any python object

    Returns:
        A list of strings representing the available attributes and methods of an object.

        """

    return dir(obj)
