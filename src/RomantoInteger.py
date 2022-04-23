# -*- coding: utf-8 -*-
"""
@author: jameswang
"""
"""
13.Roman to Integer
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Input: s = "IV"
Output: 4

For example, 2 is written as II in Roman numeral,
 just two one's added together. 12 is written as XII,
 which is simply X + II. 
 The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest 
from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, 
which is written as IX. ,D
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

"""


class Solution(object):
    def romanToInt(self, s):

        # create hash table
        roman_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # map s to list
        numbers = [roman_table[x] for x in s]

        # rule
        # has [a,b]
        # if left one smaller than right one which meaning subtraction
        # b-a or write  (-1)*a +b
        # if left one larger than right one meaning addition

        for i in range(0, len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i] *= -1
        return sum(numbers)

        # check IV
        # 1,5
        # 1<5
        # -1,5 sum([-1,5]) = 4
