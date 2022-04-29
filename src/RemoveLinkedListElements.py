# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    if not head:
        return head
    newhead = ListNode(0)
    newhead.next = head
    # check head.val is not val
    slow = newhead
    fast = head

    while fast:
        if fast.val != val:
            slow.next.val = fast.val
            slow = slow.next
        fast = fast.next

    slow.next = None

    return newhead.next
