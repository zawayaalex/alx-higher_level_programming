#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    for i in range (n):
        print("{}".format(my_list[n - 1]))
        n -= 1
