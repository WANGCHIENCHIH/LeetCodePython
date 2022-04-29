# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    iterA, iterB = headA, headB

    lenA, lenB = 0, 0

    while iterA:
        lenA += 1
        iterA = iterA.next

    while iterB:
        lenB += 1
        iterB = iterB.next

    iterA, iterB = headA, headB
    # check which long
    if (lenA - lenB) > 0:
        for _ in range((lenA - lenB)):
            iterA = iterA.next
    else:
        for _ in range(-(lenA - lenB)):
            iterB = iterB.next
    while iterA and iterB:
        if iterA == iterB:
            return iterA
        iterA = iterA.next
        iterB = iterB.next
    return None
