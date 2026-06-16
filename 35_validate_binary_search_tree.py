"""
LeetCode 98. Validate Binary Search Tree
Determine if a binary tree is a valid BST.

Approach: Recursive bound checking (min, max) for each subtree. O(n) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().isValidBST(root))  # True
