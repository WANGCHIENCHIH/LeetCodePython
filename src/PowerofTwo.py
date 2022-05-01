# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
        return False

    return bin(n).count('1') == 1
