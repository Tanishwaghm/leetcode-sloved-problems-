"""
LeetCode 21. Merge Two Sorted Lists
Merge two sorted linked lists into one sorted list.

Approach: Iterative merge with a dummy head. O(n + m) time, O(1) extra space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


def build(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    res = Solution().mergeTwoLists(l1, l2)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # [1, 1, 2, 3, 4, 4]
