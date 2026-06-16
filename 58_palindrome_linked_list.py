"""
LeetCode 234. Palindrome Linked List
Determine if a linked list reads the same forward and backward.

Approach: Find middle with slow/fast pointers, reverse second half, compare. O(n) time, O(1) space.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def build(vals):
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


if __name__ == "__main__":
    print(Solution().isPalindrome(build([1, 2, 2, 1])))  # True
