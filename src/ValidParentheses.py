# -*- coding: utf-8 -*-
"""

@author: jameswang
"""
"""
Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

1.Open brackets must be closed by the same type of brackets.
2.Open brackets must be closed in the correct order.

The stack data structure can come in handy here in representing 
this recursive structure of the problem. We can't really process this from 
the inside out because we don't have an idea about the overall structure. 
But, the stack can help us process this recursively i.e. 
from outside to inwards.
"""


# class Solution(object):
#     def isValid(self, s):

def isValid(s):
    # if len (s) is odd,not parent
    if len(s) % 2 == 1:
        return False

    # create a stack
    brackets = []

    # if bracket is '(' ,'[','{',add to stack
    # else if ')',']','}' ,match the top of stack pop top element
    # create bracket table,right bracket is key ,left bracket is value
    # example if  meet key '}' check stack top ,if is value '{' 
    # ,pop '{' out of stack
    #
    bracket_table = {'}': '{', ']': '[', ')': '('}

    for b in s:

        # check is left bracket or  right bracket
        # 　if is right bracket
        if b in bracket_table.keys():

            # check brackets stack has element or not
            if len(brackets) == 0:
                # has no element can't pop left
                return False
            # has element
            else:
                # pop top element in stack
                top_bracket = brackets.pop()
                # if pop elemement don't match dict ,they are nor parent
                if top_bracket != bracket_table[b]:
                    return False

        # if left bracket
        else:
            # add to brackets stack
            brackets.append(b)
    # if stack has element final ,is not parent        
    if len(brackets) != 0:
        return False
    else:
        return True
