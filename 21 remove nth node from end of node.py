# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # delete node
        slow.next = slow.next.next

        return dummy.next
