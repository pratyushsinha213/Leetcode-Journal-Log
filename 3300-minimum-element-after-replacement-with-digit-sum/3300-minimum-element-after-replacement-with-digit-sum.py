class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum_digits = []
        for num in nums:
            str_num = str(num)
            digit_sum = [int(i) for i in str_num]
            sum_digits.append(sum(digit_sum))
        
        return min(sum_digits)