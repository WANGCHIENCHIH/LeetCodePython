# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = []
    for y in range(rowIndex + 1):
        # add first element of subarray
        curr_row = [1]
        # deal with second or later elements
        # this range if numRows==1,just res.append[1]
        for x in range(1, y + 1):
            # if this is the end of the array
            if x == y:
                curr_row += [1]
            # if this is not the end of the array
            elif x < y:
                # add last array 's element
                curr_row += [res[y - 1][x - 1] + res[y - 1][x]]
        res.append(curr_row)

    return res[-1]
