# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.right), maxDepth(root.left))+1
    
    
