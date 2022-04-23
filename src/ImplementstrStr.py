# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def strStr(haystack, needle):
    """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
    if len(needle) == 0:
        return 0
    if len(haystack) < len(needle):
        return -1
    for headindex in range(0, len(haystack)):
        if haystack[headindex:headindex + len(needle)] == needle:
            return headindex

    return -1


print(strStr("hello", "ll"))
