"""
LeetCode 230. Kth Smallest Element in a BST
Find the k-th smallest value in a binary search tree.

Approach: Iterative in-order traversal using an explicit stack, stop at k-th pop.
O(h + k) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return -1


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(Solution().kthSmallest(root, 1))  # 1
