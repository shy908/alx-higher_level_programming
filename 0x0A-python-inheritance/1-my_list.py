#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method that sort a list"""

        print(sorted(list(self)))
