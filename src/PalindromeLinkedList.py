# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isPalindrome(head):
    if not head:
        return False
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack == stack[::-1]

# try defined two point slow and fast,do slow one step,and fast two step
