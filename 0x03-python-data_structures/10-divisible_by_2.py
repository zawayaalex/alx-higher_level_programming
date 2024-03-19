#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = [None] * len(my_list)
    if len(my_list) == 0:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] % 2 == 0:
                result[i] = True
            else:
                result[i] = False
        return result
