# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = []
    for num in nums:
        if num not in a:
            a.append(num)
        else:
            a.remove(num)
    return a[0]
