#!/usr/bin/python3
""" Module for add-integer method """

def add_integer(a, b=98):
    """ Adds two integers.

    Args:
       a: first int
       b: second int, default value 98

    Raises:
        TypeError: if a, b are neither int nor float.

    
    Returns:
        sum of a and b.
        """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
        if isinstance(b, float):
            b = int(b)
            return a + b

        if __name__ == "__main__":
            import doctest
            doctest.testfile("0-add_integer.txt")

