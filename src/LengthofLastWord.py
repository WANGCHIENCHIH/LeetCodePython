# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def lengthOfLastWord(s):
    """
        :type s: str
        :rtype: int
        """
    s = s.strip()
    return len(s.split(' ')[-1])
