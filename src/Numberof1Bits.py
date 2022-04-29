# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def hammingWeight(n):
    n = "{:32b}".format(n)
    return n.count('1')
