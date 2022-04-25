# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def hasPathSum(self, root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    if not root:
        return False

    if not root.left and not root.right:
        # the node
        if targetSum == root.val:
            return True
        else:
            return False
    else:
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
