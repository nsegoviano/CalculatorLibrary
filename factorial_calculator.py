#!/usr/bin/env python
import sys

def factorial(n):
    if n == 0:
        return 1
    # else:
    return n * factorial(n -1)
#print(factorial(n))
    
    if __name__ == '__main__':
        if len(sys.argv) > 1:
            main(int(sys.argv[1]))
