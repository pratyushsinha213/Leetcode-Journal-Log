# class SmallestInfiniteSet:

#     def __init__(self):
#         self.minHeap = [i for i in range(1, 1001)]
#         heapify(self.minHeap)

#     def popSmallest(self) -> int:
#         return heappop(self.minHeap) if len(self.minHeap) != 0 else -1

#     def addBack(self, num: int) -> None:
#         if num in set(self.minHeap):
#             return
#         heappush(self.minHeap, num)


# # Your SmallestInfiniteSet object will be instantiated and called as such:
# # obj = SmallestInfiniteSet()
# # param_1 = obj.popSmallest()
# # obj.addBack(num)

import heapq
class SmallestInfiniteSet:
    # Set of all positive integers - initialize this
    def __init__(self):
        # Set to keep removed objects
        self.removed = set()
        # Min heap of size k to track min objects
        self.minheap = list(range(1, 1001))
        heapq.heapify(self.minheap)

    # Remove and return smallest int
    def popSmallest(self) -> int:
        x = heapq.heappop(self.minheap)
        self.removed.add(x)
        return x

    # Add back a positive int num if not already in infinite set
    def addBack(self, num: int) -> None:
        if num in self.removed:
            heapq.heappush(self.minheap, num)
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)