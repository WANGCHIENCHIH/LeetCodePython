# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def reverseList(head):
    # prev_node,current_node,nextnode
    prev = None

    while head:
        next_n = head.next
        # reverse next
        head.next = prev
        # prev to current node
        prev = head
        # head to next node
        head = next_n
    # return current head
    return prev
