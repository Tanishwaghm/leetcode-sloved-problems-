"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
Rebuild a binary tree from its preorder and inorder sequences.

Approach: Recursion with a hash map for inorder index lookup. O(n) time, O(n) space.
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = index_map[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)


if __name__ == "__main__":
    tree = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(tree.val, tree.left.val, tree.right.val)  # 3 9 20
