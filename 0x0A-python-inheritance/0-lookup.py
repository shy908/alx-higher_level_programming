#!/usr/bin/python3
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
