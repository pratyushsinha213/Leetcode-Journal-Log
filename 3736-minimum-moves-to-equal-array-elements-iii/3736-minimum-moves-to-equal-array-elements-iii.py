class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_elem = max(nums)

        increase = 0
        for i in range(len(nums)):
            if nums[i] == max_elem:
                increase += 0
            else:
                increase += (max_elem-nums[i])
            
        return increase