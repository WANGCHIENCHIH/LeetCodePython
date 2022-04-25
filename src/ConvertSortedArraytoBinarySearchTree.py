# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def sortedArrayToBST(nums):
    if not nums or len(nums) == 0:
        return None
    return getNode(nums, 0, len(nums) - 1)


def getNode(nums, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    root = nums[mid]
    root.left = getNode(nums, left, mid - 1)
    root.right = getNode(nums, mid + 1, right)
    return root
