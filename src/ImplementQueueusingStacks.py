# -*- coding: utf-8 -*-
"""
@author: jameswang
"""


class MyQueue:

    def __init__(self):
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        temp = self.array[0]
        self.array.remove(temp)
        return temp

    def peek(self) -> int:
        return self.array[0]

    def empty(self) -> bool:
        return len(self.array) == 0
