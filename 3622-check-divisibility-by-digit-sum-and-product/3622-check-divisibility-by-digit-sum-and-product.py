class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(str(i)) for i in str(n)]
        sum_digits, prod_digits = 0, 1
        
        for digit in digits:
            sum_digits += digit
            prod_digits *= digit
        
        return n % (sum_digits + prod_digits) == 0