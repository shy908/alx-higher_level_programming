#!/usr/bin/python3
def print_alphabet():
    alphabet =""
    for i in range(ord('z'), ord('a') -1, -1):
        if i % 2 == 1:
            alphabet += chr(i).upper()
        else:
            alphabet += chr(i)
            print(alphabet, end="")
