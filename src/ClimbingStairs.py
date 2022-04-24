# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def climbStairs(n):
    """
        :type n: int
        :rtype: int
        """
    # init stage dp
    # for zero stage
    # for one stage [1]
    # for two stage [1,1],[2]
    dp = [0, 1, 2]
    # initial all stage from 3 stages to n stages
    for i in range(3, n + 1):
        dp.append((dp[i - 1] + dp[i - 2]))

    if n == 0:
        # never use
        return dp[0]
    elif n == 1:
        return dp[1]
    elif n == 2:
        return dp[2]
    else:
        return dp[n]

