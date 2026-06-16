"""
LeetCode 703. Kth Largest Element in a Stream
Design a class to find the k-th largest element in a stream of integers.

Approach: Min-heap of size k holding the k largest values seen so far. O(log k) per add.
"""
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    print(kl.add(3))   # 4
    print(kl.add(5))   # 5
    print(kl.add(10))  # 5
