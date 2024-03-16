#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord('c'): None})
    final = new.translate({ord('C'): None})
    return final
