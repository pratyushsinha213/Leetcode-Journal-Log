class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums)/len(nums)

        i = 1
        while True:
            if i > avg and i not in nums:
                return i
            i += 1