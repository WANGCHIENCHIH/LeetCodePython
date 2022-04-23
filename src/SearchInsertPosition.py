# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target == nums[0]:
        return 0
    if target < nums[0]:
        return 0
    if target > nums[-1]:
        return len(nums)
    lowerIndex = 0
    highIndex = len(nums)

    while lowerIndex <= highIndex:
        midIndex = (lowerIndex + highIndex) // 2
        if target == nums[midIndex]:
            return midIndex
        # highIndex=midIndex
        elif target < nums[midIndex]:
            highIndex = midIndex - 1
        else:
            lowerIndex = midIndex + 1

    return lowerIndex


