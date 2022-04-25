# -*- coding: utf-8 -*-
"""

@author: jameswang
"""


def minDepth(root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return max(minDepth(root.left), minDepth(root.right)) + 1
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1
