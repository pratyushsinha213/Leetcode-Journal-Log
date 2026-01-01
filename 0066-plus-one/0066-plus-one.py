class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1
        str_d = [str(i) for i in digits]
        incr_n = int(''.join(str_d)) + 1
        
        return [int(digit) for digit in str(incr_n)]