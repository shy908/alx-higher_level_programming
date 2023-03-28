#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            print("{}".format,end=" ")
            count += 1
        except Exception as e:
            print(e)
            if count == x:
                break
            print()
            return count
