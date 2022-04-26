# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = str(s)
    words = (''.join(filter(str.isalnum, s))).lower()
    return words == words[::-1]