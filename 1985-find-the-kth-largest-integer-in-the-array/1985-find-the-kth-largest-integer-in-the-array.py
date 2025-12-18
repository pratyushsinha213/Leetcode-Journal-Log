class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(num) for num in nums]

        heapify(nums)

        for i in range(k):
            pop = heappop(nums)
        
        return str(-pop)