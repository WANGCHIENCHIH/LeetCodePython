# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    stack = []
    if not root:
        return res

    stack.append(root)
    while stack:
        current_node = stack.pop()

        res.append(current_node.val)

        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
    return res[::-1]
