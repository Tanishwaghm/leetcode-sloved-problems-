"""
LeetCode 207. Course Schedule
Determine if it is possible to finish all courses given prerequisite pairs.

Approach: Topological sort via Kahn's algorithm (BFS with in-degree counts).
O(V + E) time, O(V + E) space.
"""
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return visited == numCourses


if __name__ == "__main__":
    print(Solution().canFinish(2, [[1, 0]]))  # True
    print(Solution().canFinish(2, [[1, 0], [0, 1]]))  # False
