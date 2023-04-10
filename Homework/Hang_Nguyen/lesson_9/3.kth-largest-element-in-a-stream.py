# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

            
    def add(self, val):
        heapq.heappush(self.pool, val)
        if len(self.pool) > self.k:
            heapq.heappop(self.pool)
        return self.pool[0]

# TEST CASE
kthLargest = KthLargest(3, [4, 5, 8, 2])

print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))