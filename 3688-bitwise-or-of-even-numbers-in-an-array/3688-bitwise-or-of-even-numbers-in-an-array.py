class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        bitwise = 0

        for num in nums:
            if num % 2 == 0:
                bitwise |= num

        return bitwise