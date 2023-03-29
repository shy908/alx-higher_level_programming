#!/usr/bin/python3
class Square:
    '''Defines Square'''
    def __init__(self, size=0):
        ''' Initializes data'''
        self.__size = size
        ''' checking data inorder to make sure that correct data has been provided'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
