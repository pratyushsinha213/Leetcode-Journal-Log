class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_count = 0

        for num in nums:
            str_n = str(num)
            if len(str_n) % 2 == 0:
                even_count += 1

        return even_count