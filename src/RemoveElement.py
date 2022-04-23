# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def removeElement(nums, val):
    currentIndex = 0
    lastIndex = len(nums)
    while currentIndex < lastIndex:
        if nums[currentIndex] == val:
            # find num to relace this
            nums[currentIndex] = nums[lastIndex - 1]

            lastIndex -= 1
        else:
            currentIndex += 1

    print(nums)

    print(lastIndex)


# removeElement([3,2,2,3], 3)
removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
