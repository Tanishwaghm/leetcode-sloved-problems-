"""
LeetCode 226. Invert Binary Tree
Invert (mirror) a binary tree.

Approach: Recursively swap left and right children. O(n) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = Solution().invertTree(root)
    print(inverted.val, inverted.left.val, inverted.right.val)  # 4 7 2
