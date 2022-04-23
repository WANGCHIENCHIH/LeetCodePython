# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def addBinary(a, b):
    ans = int(a, 2) + int(b, 2)

    test = bin(ans)[2:]
    return test


