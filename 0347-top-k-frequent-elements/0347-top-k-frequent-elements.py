class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [(-freq, num) for num, freq in counter.items()]

        heapq.heapify(arr)

        result = []
        for i in range(k):
            most_freq, num = heapq.heappop(arr)
            result.append(num)

        return result