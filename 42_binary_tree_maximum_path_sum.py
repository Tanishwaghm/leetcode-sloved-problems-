"""
LeetCode 124. Binary Tree Maximum Path Sum
Find the maximum path sum between any two nodes (path need not pass through root).

Approach: Post-order DFS returning max single-branch gain, updating a global best.
O(n) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            self.best = max(self.best, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        gain(root)
        return self.best


if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxPathSum(root))  # 42
