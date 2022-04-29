# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isIsomorphic(s, t):
    for i in range(0, len(s)):
        if s.find(s[i]) != t.find(t[i]):
            return False
    return True
