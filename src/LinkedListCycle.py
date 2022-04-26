# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
        return False
    slow = fast = head.next

    while fast and fast.next:
        fast = fast.next.next

        if fast == slow:
            return True
        slow = slow.next
    return False
