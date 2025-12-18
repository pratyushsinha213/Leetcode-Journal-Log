class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        heapq.heapify(nums)

        while nums:
            num = heapq.heappop(nums)
            res.append(num)

        return res