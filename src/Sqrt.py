# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def mySqrt(x):
    H = (x // 2) + 1
    L = 0

    while H >= L:
        middle = (H + L) // 2
        if middle * middle == x:
            return middle
        elif middle * middle > x:
            H = middle - 1
        else:
            L = middle + 1
    return H


print(mySqrt(2147395599))
