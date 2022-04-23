# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""

"""


class Solution(object):
    def longestCommonPrefix(strs):
        # first sort
        strs = sorted(strs)

        prefix_str = ""

        for index, value in enumerate(strs[0]):
            if value == max(strs)[index]:
                prefix_str += value
            else:
                break
        return prefix_str
