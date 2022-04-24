# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def isSymmetric(root):
    def isSymmetricTree(p, q):

        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            # notice that this is different with same tree
            return isSymmetricTree(p.left, q.right) and isSymmetricTree(p.right, q.left)
        return False

    if root is None:
        return True

    return isSymmetricTree(root.left, root.right)
