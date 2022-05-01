# -*- coding: utf-8 -*-
"""
@author: jameswang
"""

class MyStack:

    def __init__(self):
        self.array=[]

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        return self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def empty(self) -> bool:
        return len(self.array)==0 