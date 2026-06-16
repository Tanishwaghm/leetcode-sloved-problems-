"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree
Find the lowest common ancestor of two nodes in a binary tree.

Approach: Recursive DFS; a node is the LCA if both targets are found in different subtrees.
O(n) time, O(h) space.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1, TreeNode(0), TreeNode(8)))
    p, q = root.left, root.left.right
    print(Solution().lowestCommonAncestor(root, p, q).val)  # 5
