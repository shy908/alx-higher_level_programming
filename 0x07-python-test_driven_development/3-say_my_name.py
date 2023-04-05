#!/usr/bin/python3
"""
Say my name -A function that says your name
"""

def say_my_name(first_name, last_name=""):
    """
    say your name

    Args:
       first_name: type str
       last_name: type str

    Raises:
         TypeError: If first_name or last name is not string

    Returns:
    your name

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
