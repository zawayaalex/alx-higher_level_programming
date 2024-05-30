#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]

# File path: 1-main.py

if __name__ == "__main__":
    search_replace = __import__('1-search_replace').search_replace

    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
