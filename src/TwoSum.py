# -*- coding: utf-8 -*-
"""
@author: jameswang

1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums, target):
        # defined dict
        answers = {}

        # nums to hash table use enumerate
        for i, v in enumerate(nums):
            # i is key v is value

            another_answer = target - v
            # if another_answer in answers  meaning target= v + another_answer
            if another_answer in answers:
                return [answers[another_answer], v]

            # if another_answer not in anwers maybe it not find another v
            # add another_answer to answers
            # convert v to key ,i to value:
            answers[v] = i

        # if not found v and another_answer
        # return null list
        return []

    def twoSum2(self, nums, target):
        # defined dict
        answer = {}

        for i in range(0, len(nums)):

            if (target - nums[i]) in answer:

                return [answer[target - nums[i]], i]
            else:
                answer[nums[i]] = i

        return []
