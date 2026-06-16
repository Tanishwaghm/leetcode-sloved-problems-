"""
LeetCode 215. Kth Largest Element in an Array
Find the k-th largest element in an unsorted array.

Approach: Min-heap of size k. O(n log k) time, O(k) space.
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
