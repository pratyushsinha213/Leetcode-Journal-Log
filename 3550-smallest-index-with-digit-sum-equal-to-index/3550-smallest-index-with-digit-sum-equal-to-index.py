class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            str_n = str(nums[i])
            digits = [int(n) for n in str_n]
            sum_digits = sum(digits)

            if sum_digits == i:
                return i
        
        return -1