# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def titleToNumber(columnTitle):
    res = 0

    for a in columnTitle:
        res = res * 26 + (ord(a) - ord('A') + 1)
    return res
