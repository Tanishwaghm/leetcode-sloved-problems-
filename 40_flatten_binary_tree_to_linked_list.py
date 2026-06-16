"""
LeetCode 114. Flatten Binary Tree to Linked List
Flatten a binary tree into a "linked list" using the right pointers, preorder.

Approach: Reverse-preorder (right, left, root) iteration with a running prev pointer.
O(n) time, O(h) space for recursion.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        dfs(root)


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    Solution().flatten(root)
    out = []
    node = root
    while node:
        out.append(node.val)
        node = node.right
    print(out)  # [1,2,3,4,5,6]
