# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def inorderTraversal(root):
    res = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            # add root to stack
            stack.append(curr)
            # continue find left leaf until the end node as root
            curr = curr.left
        curr = stack.pop()
        # print(curr)
        res.append(curr.val)
        # if has no right node,next node will pop root of the end node
        curr = curr.right
    return res
