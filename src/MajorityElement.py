# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    count = 1

    for i in range(1, len(nums)):
        num = nums[i]
        if num == res:
            count += 1
        elif num != res and count > 0:
            count -= 1
        elif num != res and count == 0:
            res = num
            count = 1
    return res
