# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def lowestCommonAncestor(self, root, p, q):
    # BST value of left small than root ,value of right larger than root

    if root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root


def lowestCommonAncestor2(self, root, p, q):
    # BST value of left small than root ,value of right larger than root
    # left<= x node <=right
    # if root value is x ,p,q is left or right,
    # (p-x)*(q-x) will<0
    # if p or q is root
    # (p-x) or (q-x)==0,(p-x)*(q-x)==0
    # if x not between p,q,(p-x)*(q-x)>0
    # if x <p,x<q,it need to update root to right node
    # if x>p,x>q,it need to update root to left node
    while root:
        if (root.val - p.val) * (root.val - q.val) <= 0:
            return root
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            root = root.left
