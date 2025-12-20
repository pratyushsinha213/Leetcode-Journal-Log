class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # sort each row descending
        for row in nums:
            row.sort(reverse=True)
        
        ans = 0
        n = len(nums[0])
        
        # take max column value each round
        for col in range(n):
            ans += max(nums[row][col] for row in range(len(nums)))
        
        return ans