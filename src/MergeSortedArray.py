# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

"""
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
 You may assume that nums1 has a size equal to m + n such that 
 it has enough space to hold additional elements from nums2.
 
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

"""


def merge(nums1, m, nums2, n):
    # add pointer
    current_index = m + n - 1
    nums1_index = m - 1
    nums2_index = n - 1
    while nums1_index >= 0 and nums2_index >= 0:
        # if tail of nums1>nums2,add to answer tail
        if nums1[nums1_index] > nums2[nums2_index]:
            nums1[current_index] = nums1[nums1_index]
            # nums1 tail compared,update nums1 tail
            nums1_index -= 1
        # if tail of nums2>=nums1 add to answer tail
        else:
            nums1[current_index] = nums2[nums2_index]
            # nums2 tail compared,update nums2 tail
            nums2_index -= 1
        # answer tail add,update answertail
        current_index -= 1
    # avoid all of elements in nums1 larger than nums
    while nums2_index >= 0:
        nums1[current_index] = nums2[nums2_index]
        nums2_index -= 1
        current_index -= 1
    return nums1
