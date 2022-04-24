# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def deleteDuplicates(head):
    """
        :type head: ListNode
        :rtype: ListNode
        """
    if head is None:
        return head

    sort = head

    while sort.next is not None:
        if sort and sort.val == sort.next.val:
            sort.next = sort.next.next
        else:
            sort = sort.next
    return head
