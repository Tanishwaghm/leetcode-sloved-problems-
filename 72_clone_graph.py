"""
LeetCode 133. Clone Graph
Return a deep copy of a connected undirected graph given a reference node.

Approach: DFS with a hash map from original node to its clone, to avoid infinite loops.
O(V + E) time, O(V) space.
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        clones = {}

        def dfs(n: "Node") -> "Node":
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            clones[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


if __name__ == "__main__":
    n1, n2 = Node(1), Node(2)
    n1.neighbors.append(n2)
    n2.neighbors.append(n1)
    clone = Solution().cloneGraph(n1)
    print(clone.val, clone.neighbors[0].val)  # 1 2
