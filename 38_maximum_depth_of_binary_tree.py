"""
LeetCode 104. Maximum Depth of Binary Tree
Return the maximum depth of a binary tree.

Approach: Recursive DFS, depth = 1 + max(left, right). O(n) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().maxDepth(root))  # 3
