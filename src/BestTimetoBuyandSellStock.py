# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def maxProfit(prices):
    maxprofit = float("-inf")
    minprice = prices[0]

    for p in prices:
        if (p - minprice) > maxprofit:
            maxprofit = p - minprice

        if p < minprice:
            minprice = p
    return maxprofit


print(maxProfit([7, 1, 5, 3, 6, 4]))
