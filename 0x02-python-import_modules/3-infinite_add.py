#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = 0
    count = len(sys.argv) - 1
    for i in range(count):
        n = n + int(sys.argv[i + 1])
    print("{}".format(n))
