#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    arg = ""
    if argc <= 1:
        arg = "arguments."
    elif argc == 2:
        arg = "argument:"
    else:
        arg = "arguments:"
    print("{} {}".format((argc - 1), arg))
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
