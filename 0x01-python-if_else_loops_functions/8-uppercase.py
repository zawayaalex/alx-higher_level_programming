#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(96, 123):
            print("{}".format(chr(ord(i)-32)), end="")
    print("")
