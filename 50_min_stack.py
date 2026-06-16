"""
LeetCode 155. Min Stack
Design a stack supporting push, pop, top, and retrieving the minimum in O(1).

Approach: Auxiliary stack storing running minimums alongside the main stack.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())  # -3
    ms.pop()
    print(ms.top())     # 0
    print(ms.getMin())  # -2
