# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when 
it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.

Follow up: Could you solve it 
without converting the integer to a string?
"""


class Solution(object):
    def isPalindrome(self, x):
        # if x<0  is not palindrome
        if x < 0:
            return bool(0)
        else:
            temp = x
            # ban string reverse method
        # temp = int(str(temp)[::-1])
        # try mod
        # ex: 12 % 10 = 2
        reverse_num = 0
        # if temp = 12
        while temp > 0:
            remainder = temp % 10  # remainder= 12%10=2
            # reverse number= 0*10+2 =2
            # if next temp =1
            # next remainder = 1% 10=1
            # next reverse_number= 2*10+1=21
            # check next_next_temp 1//10=0
            # next_next_temp will stop while loop
            # reverse finish
            reverse_num = reverse_num * 10 + remainder
            # update temp
            temp //= 10
        # after reverse check is palindrome?
        if x == reverse_num:
            return bool(1)
        else:
            return bool(0)
