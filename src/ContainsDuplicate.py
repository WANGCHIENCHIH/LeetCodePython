# -*- coding: utf-8 -*-
"""

@author: jameswang
"""


def containsDuplicate(nums):
    s = set(nums)
    return len(s) != len(nums)
