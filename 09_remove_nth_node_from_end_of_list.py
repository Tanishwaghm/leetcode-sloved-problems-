"""
LeetCode 19. Remove Nth Node From End of List
Remove the n-th node from the end of a linked list and return its head.

Approach: Dummy head + fast/slow pointers, one pass. O(n) time, O(1) space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


def build(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    res = Solution().removeNthFromEnd(head, 2)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # [1, 2, 3, 5]
