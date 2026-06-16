"""
LeetCode 269. Alien Dictionary
Derive a valid character ordering of an alien alphabet given a sorted word list.

Approach: Build a graph of "comes before" relations between adjacent letters,
then topologically sort with Kahn's algorithm. O(C) time where C = total chars.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}

        for first, second in zip(words, words[1:]):
            min_len = min(len(first), len(second))
            found_diff = False
            for i in range(min_len):
                c1, c2 = first[i], second[i]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    found_diff = True
                    break
            if not found_diff and len(second) < len(first):
                return ""

        queue = deque([ch for ch in indegree if indegree[ch] == 0])
        order = []
        while queue:
            ch = queue.popleft()
            order.append(ch)
            for nxt in graph[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(indegree):
            return ""
        return "".join(order)


if __name__ == "__main__":
    print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # "wertf"
