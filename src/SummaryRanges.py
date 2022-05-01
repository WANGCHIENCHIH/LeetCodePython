# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def summaryRanges(nums):
    myrange = []
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums) and nums[j] - nums[j - 1] == 1:
            j += 1
        if i + 1 < j:
            myrange.append("{a}->{b}".format(a=nums[i], b=nums[j - 1]))
        else:
            myrange.append(str(nums[i]))
        i = j
    return myrange
