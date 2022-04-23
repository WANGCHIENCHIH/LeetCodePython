# -*- coding: utf-8 -*-
"""
@author: jameswang
"""
"""
#20211011版本，速度待加強
"""
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    currentIndex = 0
    nextIndex = currentIndex + 1
    while nextIndex < len(nums):
        if nums[nextIndex] != nums[currentIndex]:
            nums[currentIndex + 1] = nums[nextIndex]
            currentIndex += 1
        nextIndex += 1
    return currentIndex + 1
# removeDuplicates([1,1,2])
