#!/usr/bin/python3
def islower(c):
    if ord(c) > 96 and ord(c) < 124:
        print(c, "is lower")
        return True
    else:
        print(c, "is upper")
        return False
