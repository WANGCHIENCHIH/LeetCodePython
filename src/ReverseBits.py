# -*- coding: utf-8 -*-
"""
@author: jameswang
"""
"""
def reverseBits(self, n: int) -> int:
    return int("{:032b}".format(n)[::-1],2)':032b'.format(n)[::-1],2)
"""


def reverseBits(n):
    n = "{:32b}".format(n)
    n = n[::-1]
    print(int(n, 2))


a = 0b00000010100101000001111010011100
reverseBits(a)
