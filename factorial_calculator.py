#!/usr/bin/env python
import sys

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
