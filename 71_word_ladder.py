"""
LeetCode 127. Word Ladder
Find the length of the shortest transformation sequence from beginWord to endWord.

Approach: BFS over the word graph, generating neighbors by single-letter substitution.
O(n * 26 * L) time.
"""
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue
                    candidate = word[:i] + ch + word[i + 1:]
                    if candidate in word_set and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, steps + 1))
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
