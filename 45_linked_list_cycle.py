"""
LeetCode 141. Linked List Cycle
Determine if a linked list has a cycle.

Approach: Floyd's slow/fast pointer technique. O(n) time, O(1) space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    b.next = a
    print(Solution().hasCycle(a))  # True
