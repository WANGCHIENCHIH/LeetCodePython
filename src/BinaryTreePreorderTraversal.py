# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []  # get val
    stack = []

    while root or stack:

        while root:
            # mid,left,right
            result.append(root.val)
            stack.append(root)

            root = root.left
        # right
        root = stack.pop()
        root = root.right
    return result
