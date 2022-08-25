#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program"""

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
