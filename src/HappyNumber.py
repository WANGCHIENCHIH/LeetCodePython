# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isHappy(n):
    if n == 1:
        return True
    stack = []

    while n not in stack:
        stack.append(n)

        # count sum of square
        n = sum([int(x) ** 2 for x in str(n)])
        if n == 1:
            return True
    return False
