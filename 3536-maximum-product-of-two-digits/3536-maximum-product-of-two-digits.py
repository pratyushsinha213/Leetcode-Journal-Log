class Solution:
    def maxProduct(self, n: int) -> int:
        str_n = str(n)
        digits = [int(digit) for digit in str_n]

        max_prod = 0
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                prod = digits[i] * digits[j]
                max_prod = max(prod, max_prod)
            
        return max_prod