# -*- coding: utf-8 -*-
"""

@author: jameswang
"""


def containsNearbyDuplicate(nums, k):
    mydict = {}
    for i in range(len(nums)):
        if nums[i] not in mydict or (i - mydict[nums[i]]) > k:
            mydict[nums[i]] = i
        else:
            return True
    return False
