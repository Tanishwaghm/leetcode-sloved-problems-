"""
LeetCode 2. Add Two Numbers
Add two numbers represented as reversed-order linked lists.

Approach: Simulate elementary addition with carry. O(n) time, O(n) space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


def build(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    l1 = build([2, 4, 3])
    l2 = build([5, 6, 4])
    res = Solution().addTwoNumbers(l1, l2)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # [7, 0, 8]
