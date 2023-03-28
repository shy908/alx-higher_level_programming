#!/usr/bin/python3
def safe_print_division(a, b):
    '''
    divide two integers and print the result ,use except to catch zero division error
    '''
    try:
        result = a/b
    except:
        result = None
    finally:
        print("Inside result:{}".format(result))
        return result
