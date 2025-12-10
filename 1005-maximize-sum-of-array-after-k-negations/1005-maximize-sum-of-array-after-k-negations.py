class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            min_elem = min(nums)
            idx = nums.index(min_elem)
            nums[idx] = -nums[idx]
        
        return sum(nums)