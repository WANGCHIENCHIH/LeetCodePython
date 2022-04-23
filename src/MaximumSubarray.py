# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def crossMaxcount(nums, start, middle, end):
    currentLeftMax = nums[middle]
    currentRightMax = nums[middle + 1]

    currentLeftSum, currentRightSum = 0, 0

    i, j = middle, middle + 1
    while i >= start:
        currentLeftSum += nums[i]

        currentLeftMax = max(currentLeftMax, currentLeftSum)

        i -= 1
    while j <= end:
        currentRightSum += nums[j]
        currentRightMax = max(currentRightMax, currentRightSum)

        j += 1

    return max([currentLeftMax, currentRightMax, (currentLeftMax + currentRightMax)])


def DivideandConquer(nums, start, end):
    """
    start: represent nums first element index
    end: represent nums last element index
    """
    if start == end:
        # this mean nums only has one element
        return nums[start]

    middleIndex = (start + end) // 2

    # count left max from index 0 to middle
    leftMax = DivideandConquer(nums, start, middleIndex)
    # count left max from index middle+1 to end
    rightMax = DivideandConquer(nums, middleIndex + 1, end)

    crossMax = crossMaxcount(nums, start, middleIndex, end)

    return max([leftMax, rightMax, crossMax])


def GetMax(nums):
    return DivideandConquer(nums, 0, len(nums) - 1)


# O(n2)

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    maxtotal = -(10 ** 4) - 1
    i = 0
    while i < len(nums):

        for j in range(i + 1, len(nums) + 1):
            maxtotal = max(maxtotal, sum(nums[i:j]))
        i += 1
    return maxtotal


# print(maxSubArray([1]))
# print(maxSubArray([5,4,-1,7,8]))
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(GetMax([1]))
print(GetMax([5, 4, -1, 7, 8]))
print(GetMax([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(GetMax([7, 1, 5, 3, 6, 4]))
# -2 1 -3 4 -1 2 1 -5 4
